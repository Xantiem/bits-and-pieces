#include <stdio.h>

#include "pico/stdlib.h"

int main( void )
{
    const uint LED_PIN_22 = 22;
    const uint LED_PIN_21 = 21;
    gpio_init(LED_PIN_21);
    gpio_init(LED_PIN_22);

    gpio_set_dir(LED_PIN_22, GPIO_OUT);
    gpio_set_dir(LED_PIN_21, GPIO_OUT);
    while (true) {
        gpio_put(LED_PIN_21, 0);
        gpio_put(LED_PIN_22, 1);
        sleep_ms(250);
        gpio_put(LED_PIN_22, 0);
        gpio_put(LED_PIN_21, 1);
        sleep_ms(250); 
    }
}
