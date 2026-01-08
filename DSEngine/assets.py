import os
import pygame

class AssetManager:
    IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.bmp', '.gif'}
    SOUND_EXTENSIONS = {'.wav', '.ogg'}
    MUSIC_EXTENSIONS = {'.mp3', '.ogg', '.mod', '.xm'}

    def __init__(self, base_path="assets"):
        self.base_path = base_path
        self.textures = {}
        self.sounds = {}
        self.music_tracks = {}
        self.other_files = {}
        # self.animations = {} # TODO add JSON animation support

    def load_assets(self):
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                rel_path_from_base = os.path.relpath(os.path.join(root, file), self.base_path)
                key = os.path.splitext(rel_path_from_base)[0].replace("\\", "/")  # Normalize

                full_path = os.path.join(root, file)

                if ext in self.IMAGE_EXTENSIONS:
                    self._load_texture(key, full_path)
                elif ext in self.SOUND_EXTENSIONS:
                    self._load_sound(key, full_path)
                elif ext in self.MUSIC_EXTENSIONS:
                    self.music_tracks[key] = full_path
                else:
                    self.other_files[key] = full_path

    def _load_texture(self, key, path):
        try:
            image = pygame.image.load(path).convert_alpha()
            self.textures[key] = image
        except pygame.error as e:
            print(f"[ERROR] Failed to load texture '{path}': {e}")

    def _load_sound(self, key, path):
        try:
            sound = pygame.mixer.Sound(path)
            self.sounds[key] = sound
        except pygame.error as e:
            print(f"[ERROR] Failed to load sound '{path}': {e}")

    def get_texture(self, name):
        return self.textures.get(name)

    def get_sound(self, name):
        return self.sounds.get(name)

    def play_music(self, name, loops=-1):
        file_path = self.music_tracks.get(name)
        if file_path:
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play(loops)
            except pygame.error as e:
                print(f"[ERROR] Failed to play music '{file_path}': {e}")
        else:
            print(f"[ERROR] Music track '{name}' not loaded.")

    def stop_music(self):
        pygame.mixer.music.stop()

    def __str__(self):
        result = "Asset Manager\n"
        result += "Base Path:" + self.base_path + "\n"
        result += f"{self.textures}\n"

        return result
