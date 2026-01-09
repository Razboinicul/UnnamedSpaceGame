#include "tokenizer.h"
#include <stdlib.h>
#include <stdio.h>

int main() {
  int token_count = 0;
  Token* tkns = tokenize_file("test.dasm", &token_count);
  
  printf_s("Token Count: %i\n", token_count);

  for (int i = 0; i < token_count; i++ ) {
    printf_s("Token:\nType:%d\nValue: %s\n\n", tkns[i].type, tkns[i].data);
  }

  free(tkns);
  return 0;
}