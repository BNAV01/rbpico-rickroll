import sys

def generate_pico_code(text):
    # Diccionario de mapeo: Carácter -> (HID_KEY, MODIFICADOR)
    # Ajustado para teclado ESPAÑOL (QWERTY ES)
    mapping = {
        'a': ('HID_KEY_A', '0'), 'b': ('HID_KEY_B', '0'), 'c': ('HID_KEY_C', '0'),
        'd': ('HID_KEY_D', '0'), 'e': ('HID_KEY_E', '0'), 'f': ('HID_KEY_F', '0'),
        'g': ('HID_KEY_G', '0'), 'h': ('HID_KEY_H', '0'), 'i': ('HID_KEY_I', '0'),
        'j': ('HID_KEY_J', '0'), 'k': ('HID_KEY_K', '0'), 'l': ('HID_KEY_L', '0'),
        'm': ('HID_KEY_M', '0'), 'n': ('HID_KEY_N', '0'), 'o': ('HID_KEY_O', '0'),
        'p': ('HID_KEY_P', '0'), 'q': ('HID_KEY_Q', '0'), 'r': ('HID_KEY_R', '0'),
        's': ('HID_KEY_S', '0'), 't': ('HID_KEY_T', '0'), 'u': ('HID_KEY_U', '0'),
        'v': ('HID_KEY_V', '0'), 'w': ('HID_KEY_W', '0'), 'x': ('HID_KEY_X', '0'),
        'y': ('HID_KEY_Y', '0'), 'z': ('HID_KEY_Z', '0'),
        'A': ('HID_KEY_A', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'B': ('HID_KEY_B', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'C': ('HID_KEY_C', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'D': ('HID_KEY_D', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'E': ('HID_KEY_E', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'F': ('HID_KEY_F', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'G': ('HID_KEY_G', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'H': ('HID_KEY_H', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'I': ('HID_KEY_I', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'J': ('HID_KEY_J', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'K': ('HID_KEY_K', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'L': ('HID_KEY_L', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'M': ('HID_KEY_M', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'N': ('HID_KEY_N', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'O': ('HID_KEY_O', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'P': ('HID_KEY_P', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'Q': ('HID_KEY_Q', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'R': ('HID_KEY_R', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'S': ('HID_KEY_S', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'T': ('HID_KEY_T', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'U': ('HID_KEY_U', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'V': ('HID_KEY_V', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'W': ('HID_KEY_W', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'X': ('HID_KEY_X', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'Y': ('HID_KEY_Y', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        'Z': ('HID_KEY_Z', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        '1': ('HID_KEY_1', '0'), '2': ('HID_KEY_2', '0'), '3': ('HID_KEY_3', '0'),
        '4': ('HID_KEY_4', '0'), '5': ('HID_KEY_5', '0'), '6': ('HID_KEY_6', '0'),
        '7': ('HID_KEY_7', '0'), '8': ('HID_KEY_8', '0'), '9': ('HID_KEY_9', '0'),
        '0': ('HID_KEY_0', '0'),
        '.': ('HID_KEY_PERIOD', '0'),
        ':': ('HID_KEY_PERIOD', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        '/': ('HID_KEY_7', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        '-': ('HID_KEY_SLASH', '0'),
        '_': ('HID_KEY_SLASH', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        '=': ('HID_KEY_0', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        '?': ('HID_KEY_MINUS', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        '&': ('HID_KEY_6', 'KEYBOARD_MODIFIER_LEFTSHIFT'),
        ' ': ('HID_KEY_SPACE', '0'),
    }

    output = []
    output.append("// --- PAYLOAD GENERADO ---")
    
    for char in text:
        if char in mapping:
            key, mod = mapping[char]
            output.append(f"send_key({key}, {mod}); // '{char}'")
        else:
            output.append(f"// Carácter '{char}' no soportado")
            
    output.append("send_key(HID_KEY_ENTER, 0);")
    output.append("// ------------------------")
    
    return "\n".join(output)

if __name__ == "__main__":
    url = input("Introduce la URL o texto para el payload: ")
    payload_code = generate_pico_code(url)
    
    with open("payload.txt", "w") as f:
        f.write(payload_code)
        
    print("\n¡Listo! El código se ha guardado en 'payload.txt'")
    print("Copia el contenido y pégalo en tu main.c")