<template>
    <mycomponent
        :name="'circle' + index % 2"
    />
</template>

<script>
import mycomponent from './myComponent.vue'
import { ref } from 'vue'

export default {
    components: {
        mycomponent
    },
    setup() {
        const index = ref(0);
        setInterval(() => index.value++, 1000);

        return {
            index,
        }
    },
}
</script>
