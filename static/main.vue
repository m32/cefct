<template>
    <xbutton />
    <mycomponent :name="'circle' + (index % 2)" />
    <clock />
</template>

<script>
import { ref } from 'vue';
import mycomponent from './myComponent.vue';
import clock from './clock.vue';
import xbutton from './button.vue';

export default {
    components: {
        mycomponent,
        clock,
        xbutton
    },
    setup() {
        const index = ref(0);
        setInterval(() => index.value++, 1000);

        return {
            index
        };
    }
};
</script>
