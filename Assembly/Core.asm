BITS 16
[org 0x7c00]

call Clear
mov si, BootString
call PrintString
call Input
call PrintChar

jmp $

Clear:
    mov ax, 0x003
    int 0x10
    ret

PrintString:
    ;Takes an Address from SI and prints the string that's behind it.
    mov ax, [si];Read one Char from the string.
    inc si ;Increment si by 1 to move on to the next Char.
    cmp ax, "+"
    je Exit
    call PrintChar ;Print the Char that's currently in ax.
    jmp PrintString

PrintChar:
    ;Takes Input from ax (low bits) and prints it.
    mov ah, 0x0E
    mov bx, 0x00
    int 0x10
    ret

Input:
    mov ah, 0x0a
    int 0x21
    ret

Exit:
    ;A funtion to move up one layer.
    ret

times 400-($-$$) db 0
BootString: db "A", "+"
times 510-($-$$) db 0
dw 0xAA55 