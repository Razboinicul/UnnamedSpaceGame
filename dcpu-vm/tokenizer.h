#ifndef TOKENIZER_H
#define TOKENIZER_H

#include <stdint.h>

typedef enum {
  IDENTIFIER,
  COLON,
  REGISTER,
  COMMA,
  LBRACKET,
  RBRACKET,
  PLUS,
  UNKNOWN,
} TokenType;

typedef struct {
  char data[50];
  TokenType type;
} Token;

void append_token(Token tk, Token **tokens, uint16_t *token_count, uint16_t *current_token_position);
void create_and_append_token(TokenType type, const char *data, Token **tokens, uint16_t *token_count, uint16_t *current_token_position);
Token* tokenize_file(char *file_name, int* token_count);

#endif