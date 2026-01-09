#include "tokenizer.h"
#include <corecrt.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool char_in_array(char c, char *array, unsigned int length) {
  for (int i = 0; i < length; i++) {
    if (c == array[i]) {
      return true;
    }
  }
  return false;
}

bool char_between_range(char c, char start, char end) {
  if((c < start && c < end) || (c > start && c > end)) {
    return false;
  }
  else {
    return true;
  }
}

void append_token(Token tk, Token **tokens, uint16_t *token_count, uint16_t *current_token_position) {
  // Check for overflow first
  if (*current_token_position >= *token_count) {
      Token *new_ptr = realloc(*tokens, (*token_count + 50) * sizeof(Token));
      if (!new_ptr) {
          // Handle allocation failure
          fprintf(stderr, "Out of memory!\n");
          exit(1);
      }
      *tokens = new_ptr;
      *token_count += 50;
  }

  // Add the token
  (*tokens)[*current_token_position] = tk;
  *current_token_position += 1;
}

// Helper function to create and append a token
void create_and_append_token(TokenType type, const char *data, Token **tokens, uint16_t *token_count, uint16_t *current_token_position) {
  Token new_token;
  new_token.type = type;
  if (strcpy_s(new_token.data, sizeof(new_token.data), data) != 0) {
      fprintf(stderr, "Error copying string into token\n");
      exit(1);
  }
  append_token(new_token, tokens, token_count, current_token_position);
}

Token* tokenize_file(char *file_name, int *token_count) {
  uint16_t actual_token_count = 100;
  uint16_t current_token_position = 0;
  Token *ptr_tokens = malloc(sizeof(Token) * actual_token_count);

  FILE *fp;
  if (fopen_s(&fp, file_name, "r") != 0 || !fp) {
    fprintf(stderr, "Failed to open file: %s\n", file_name);
    return NULL;
  }

  char buffer[256];
  char temp_identifier[50] = {0};
  bool finding_identifiers = false;

  char register_array[] = {'A', 'B', 'C', 'X', 'Y', 'Z', 'I', 'J'};

  while (fgets(buffer, sizeof(buffer), fp)) {
    size_t len = strlen(buffer);
    for (size_t i = 0; i < len; i++) {
      char c = buffer[i];

      // Break on newline or comment
      if (c == '\n' || c == ';') break;

      // Handle colon
      if (c == ':') {
        if (temp_identifier[0] != '\0') {
          create_and_append_token(IDENTIFIER, temp_identifier, &ptr_tokens, &actual_token_count, &current_token_position);
          temp_identifier[0] = '\0';
          finding_identifiers = false;
        }
        char src[] = {c, '\0'};
        create_and_append_token(COLON, src, &ptr_tokens, &actual_token_count, &current_token_position);
        continue;
      }

      // Handle single-character tokens
      if (c == '+' || c == '[' || c == ']') {
          if (temp_identifier[0] != '\0') {
            create_and_append_token(IDENTIFIER, temp_identifier, &ptr_tokens, &actual_token_count, &current_token_position);
            temp_identifier[0] = '\0';
            finding_identifiers = false;
          }
          char src[] = {c, '\0'};
          create_and_append_token((c == '+') ? PLUS : (c == '[') ? LBRACKET : RBRACKET, src, &ptr_tokens, &actual_token_count, &current_token_position);
          continue;
      }

      // Handle spaces and commas
      if (c == ' ' || c == ',') {
          if (temp_identifier[0] != '\0') {
            create_and_append_token(IDENTIFIER, temp_identifier, &ptr_tokens, &actual_token_count, &current_token_position);
            temp_identifier[0] = '\0';
            finding_identifiers = false;
          }
          if (c == ',') {
            char src[] = {c, '\0'};
            create_and_append_token(COMMA, src, &ptr_tokens, &actual_token_count, &current_token_position);
          }
          continue;
      }

      // Handle registers
      if (!finding_identifiers && char_in_array(c, register_array, sizeof(register_array) / sizeof(char))) {
          if (i + 1 >= len || (!char_between_range(buffer[i+1], 'A', 'Z') && !char_between_range(buffer[i+1], 'a', 'z'))) {
            if (temp_identifier[0] != '\0') {
              create_and_append_token(IDENTIFIER, temp_identifier, &ptr_tokens, &actual_token_count, &current_token_position);
              temp_identifier[0] = '\0';
              finding_identifiers = false;
            }
            char src[] = {c, '\0'};
            create_and_append_token(REGISTER, src, &ptr_tokens, &actual_token_count, &current_token_position);
            continue;
          }
      }

      // Otherwise, append to identifier
      size_t current_len = strlen(temp_identifier);
      if (current_len < sizeof(temp_identifier) - 1) {
        temp_identifier[current_len] = c;
        temp_identifier[current_len + 1] = '\0';
        finding_identifiers = true;
      }
    }
  }

  // Flush any remaining identifier
  if (temp_identifier[0] != '\0') {
      create_and_append_token(IDENTIFIER, temp_identifier, &ptr_tokens, &actual_token_count, &current_token_position);
  }

  fclose(fp);

  // Return the actual number of tokens
  *token_count = current_token_position;
  return ptr_tokens;
}