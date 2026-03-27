#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "pico/stdlib.h"
#include "bsp/board.h"
#include "tusb.h"
#include "usb_descriptors.h"

const uint LED_PIN = 25;


void send_key(uint8_t keycode, uint8_t modifier) {
    uint8_t keycodes[6] = {keycode, 0, 0, 0, 0, 0};
    tud_hid_keyboard_report(0, modifier, keycodes); 
    board_delay(1);
    tud_hid_keyboard_report(0, 0, NULL);
    board_delay(1);
}

int main(void) {
    board_init();
    tusb_init();

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    
    for(int i=0; i<5; i++) {
        gpio_put(LED_PIN, 1); board_delay(100);
        gpio_put(LED_PIN, 0); board_delay(100);
    }

    bool atacado = false;

    while (1) {
        tud_task(); 

        if (tud_mounted() && tud_hid_ready() && !atacado) {
            gpio_put(LED_PIN, 1);
            
            board_delay(2500); 

            tud_hid_keyboard_report(0, KEYBOARD_MODIFIER_LEFTGUI, NULL);
            board_delay(5);
            uint8_t r_key[6] = {HID_KEY_R, 0, 0, 0, 0, 0};
            tud_hid_keyboard_report(0, KEYBOARD_MODIFIER_LEFTGUI, r_key);
            board_delay(5);
            tud_hid_keyboard_report(0, 0, NULL);
            
            board_delay(100); 

            send_key(HID_KEY_H, 0); send_key(HID_KEY_T, 0); send_key(HID_KEY_T, 0);
            send_key(HID_KEY_P, 0); send_key(HID_KEY_S, 0);

            send_key(HID_KEY_PERIOD, KEYBOARD_MODIFIER_LEFTSHIFT);

            send_key(HID_KEY_7, KEYBOARD_MODIFIER_LEFTSHIFT);
            send_key(HID_KEY_7, KEYBOARD_MODIFIER_LEFTSHIFT);

            send_key(HID_KEY_W, 0); 
            send_key(HID_KEY_W, 0); send_key(HID_KEY_W, 0);
            send_key(HID_KEY_PERIOD, 0);
            send_key(HID_KEY_Y, 0); send_key(HID_KEY_O, 0); send_key(HID_KEY_U, 0);
            send_key(HID_KEY_T, 0); send_key(HID_KEY_U, 0); send_key(HID_KEY_B, 0);
            send_key(HID_KEY_E, 0); send_key(HID_KEY_PERIOD, 0);
            send_key(HID_KEY_C, 0); send_key(HID_KEY_O, 0); send_key(HID_KEY_M, 0);

            send_key(HID_KEY_7, KEYBOARD_MODIFIER_LEFTSHIFT);

            send_key(HID_KEY_W, 0); send_key(HID_KEY_A, 0); send_key(HID_KEY_T, 0);
            send_key(HID_KEY_C, 0); send_key(HID_KEY_H, 0);

            send_key(HID_KEY_MINUS, KEYBOARD_MODIFIER_LEFTSHIFT);

            send_key(HID_KEY_V, 0);

            send_key(HID_KEY_0, KEYBOARD_MODIFIER_LEFTSHIFT);

            send_key(HID_KEY_D, 0);
            send_key(HID_KEY_Q, KEYBOARD_MODIFIER_LEFTSHIFT);
            send_key(HID_KEY_W, 0);
            send_key(HID_KEY_4, 0);
            send_key(HID_KEY_W, 0);
            send_key(HID_KEY_9, 0);
            send_key(HID_KEY_W, KEYBOARD_MODIFIER_LEFTSHIFT);
            send_key(HID_KEY_G, 0);
            send_key(HID_KEY_X, KEYBOARD_MODIFIER_LEFTSHIFT);
            send_key(HID_KEY_C, 0);
            send_key(HID_KEY_Q, KEYBOARD_MODIFIER_LEFTSHIFT);

            board_delay(25);
            send_key(HID_KEY_ENTER, 0);

            atacado = true;
            gpio_put(LED_PIN, 0);
        }
    }
    return 0;
}

uint16_t tud_hid_get_report_cb(uint8_t instance, uint8_t report_id, hid_report_type_t report_type, uint8_t* buffer, uint16_t reqlen) {
    (void) instance; (void) report_id; (void) report_type; (void) buffer; (void) reqlen;
    return 0;
}
void tud_hid_set_report_cb(uint8_t instance, uint8_t report_id, hid_report_type_t report_type, uint8_t const* buffer, uint16_t bufsize) {
    (void) instance; (void) report_id; (void) report_type; (void) buffer; (void) bufsize;
}
