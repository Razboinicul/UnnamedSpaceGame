#ifndef DCPU_H_
#define DCPU_H_

#include <stdint.h>

typedef uint16_t u16;

typedef struct {  
  u16 ram[65536];
  u16 a, b, c, x, y, z, i, j;
  u16 pc, sp, ex, ia;
} DCPU_VM;

typedef enum {
  // register
  REG_A, // 0x00
  REG_B, // 0x01
  REG_C, // 0x02
  REG_X, // 0x03
  REG_Y, // 0x04
  REG_Z, // 0x05
  REG_I, // 0x06
  REG_J, // 0x07
  // [register]
  ADDR_REG_A, // 0x08
  ADDR_REG_B, // 0x09
  ADDR_REG_C, // 0x0a
  ADDR_REG_X, // 0x0b
  ADDR_REG_Y, // 0x0c
  ADDR_REG_Z, // 0x0d
  ADDR_REG_I, // 0x0e
  ADDR_REG_J, // 0x0f
  // [register + next word]
  ADDR_REG_A_PLUS_WORD, // 0x10
  ADDR_REG_B_PLUS_WORD, // 0x11
  ADDR_REG_C_PLUS_WORD, // 0x12
  ADDR_REG_X_PLUS_WORD, // 0x13
  ADDR_REG_Y_PLUS_WORD, // 0x14
  ADDR_REG_Z_PLUS_WORD, // 0x15
  ADDR_REG_I_PLUS_WORD, // 0x16
  ADDR_REG_J_PLUS_WORD, // 0x17
  // (PUSH / [--SP]) if in b, or (POP / [SP++]) if in a
  PUSH_POP, // 0x18
  // [SP] / PEEK
  PEEK, // 0x19 
  // [SP + next word] / PICK n
  PICK_N, // 0x1a
  SP, // 0x1b
  PC, // 0x1c
  EX, // 0x1d
  // [next word]
  ADDR_NEXT_WORD, // 0x1e
  LIT_NEXT_WORD, // 0x1f
  // Literal value for 0xffff - 0x1e (-1, 30)
  LIT_NEG_1, // 0x20
  LIT_0, // 0x21
  LIT_1, // 0x22
  LIT_2, // 0x23
  LIT_3, // 0x24
  LIT_4, // 0x25
  LIT_5, // 0x26
  LIT_6, // 0x27
  LIT_7, // 0x28
  LIT_8, // 0x29
  LIT_9, // 0x2a
  LIT_10, // 0x2b
  LIT_11, // 0x2c
  LIT_12, // 0x2d
  LIT_13, // 0x2e
  LIT_14, // 0x2f
  LIT_15, // 0x30
  LIT_16, // 0x31
  LIT_17, // 0x32
  LIT_18, // 0x33
  LIT_19, // 0x34
  LIT_20, // 0x35
  LIT_21, // 0x36
  LIT_22, // 0x37
  LIT_23, // 0x38
  LIT_24, // 0x39
  LIT_25, // 0x3a
  LIT_26, // 0x3b
  LIT_27, // 0x3c
  LIT_28, // 0x3d
  LIT_29, // 0x3e
  LIT_30, // 0x3f
} Value;

typedef enum {
  NA,
  SET,
  ADD,
  SUB,
  MUL,
  DIV,
  DVI,
  MOD,
  MDI,
  AND,
  XOR,
  SHR,
  ASR,
  SHL,
  IFB,
  IFC,
  IFE,
  IFN,
  IFG,
  IFA,
  IFL,
  IFU,
  EMPTY_1,
  EMPTY_2,
  ADX,
  SBX,
  EMPTY_3,
  EMPTY_4,
  STI,
  STD,
} BasicOpcode;

typedef enum {
  NA = 0x00,
  JSR = 0x01,
} SpecialOpcode;

#endif