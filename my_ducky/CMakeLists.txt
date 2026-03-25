cmake_minimum_required(VERSION 3.13)

include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

project(my_ducky C CXX ASM)

pico_sdk_init()

include_directories(${CMAKE_CURRENT_LIST_DIR})

add_executable(my_ducky 
    main.c 
    usb_descriptors.c
)

# Enlaza las librerías necesarias para TinyUSB y la Pico
target_link_libraries(my_ducky pico_stdlib tinyusb_device tinyusb_board)

# Habilita la salida por USB (para ver prints en consola si quieres)
pico_enable_stdio_usb(my_ducky 1)
pico_enable_stdio_uart(my_ducky 0)

# Genera el archivo .uf2 automáticamente
pico_add_extra_outputs(my_ducky)
