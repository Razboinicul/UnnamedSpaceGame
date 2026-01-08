# Base code for an ECS that the user will call to setup an ECS for their game
class Entity:
    def __init__(self, id, name = None, group = None):
        self.id = id
        self.components = {}
        self.name = name
        self.group = group

    # Checks if the entity has a specific component instance or type
    def has_component(self, component) -> bool:
        return type(component) in self.components

    # Checks if the entity has all components in a given list
    def has_components(self, components: list) -> bool:
        return all(comp in self.components for comp in components)
    
    def add_component(self, component):
        self.components[type(component)] = component

    def remove_component(self, component):
        del(self.components, component)

# This manages all the entities in the scene
class EntityManager:
    def __init__(self):
        self.next_entity_id = 0
        self.entities: dict[int, Entity] = {}

        # Below is the cache for when we add a new entity, we can then store then here for faster lookup
        self.name_map = {}            
        self.group_map = {}

        # This is used to reduce memory, so we can shared ids, when entities are removed from the scene
        self.free_ids = []

    def create_new_entity(self, name=None, group=None) -> Entity:
        if self.free_ids:
            entity_id = self.free_ids.pop()
        else:
            entity_id = self.next_entity_id
            self.next_entity_id += 1

        entity = Entity(entity_id, name, group)
        self.entities[entity_id] = entity

        # Index by name
        if name:
            self.name_map[name] = entity_id

        # Index by group
        if group:
            if group not in self.group_map:
                self.group_map[group] = set()
            self.group_map[group].add(entity_id)

        return entity

    def get_entity_by_id(self, entity_id: int) -> Entity:
        return self.entities.get(entity_id)

    def get_entity_by_name(self, name: str) -> Entity:
        entity_id = self.name_map.get(name)
        return self.entities.get(entity_id) if entity_id is not None else None

    def get_entities_by_group(self, group: str):
        entity_ids = self.group_map.get(group, set())
        return [self.entities[entity_id] for entity_id in entity_ids if entity_id in self.entities]

    def remove_entity_by_id(self, entity_id: int):
        entity = self.entities.pop(entity_id, None)
        if entity:
            # Reuse ID
            self.free_ids.append(entity_id)

            # Clean up name index
            if entity.name and entity.name in self.name_map:
                del self.name_map[entity.name]

            # Clean up group index
            if entity.group and entity.group in self.group_map:
                self.group_map[entity.group].discard(entity_id)
                if not self.group_map[entity.group]:
                    del self.group_map[entity.group]

    def remove_entity_by_name(self, name: str):
        entity_id = self.name_map.get(name)
        if entity_id is not None:
            self.remove_entity_by_id(entity_id)

    def remove_group_of_entities(self, group: str):
        entity_ids = self.group_map.get(group, set()).copy()
        for entity_id in entity_ids:
            self.remove_entity_by_id(entity_id)
