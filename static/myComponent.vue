<template>
    <span v-html="svg" />
</template>
<script>
import { ref, watch } from 'vue'

class test {

}

console.log(test)

function asyncToRef(callback) {
    const val = ref();
    watch(() => callback(), promise => promise.then(value => val.value = value), { immediate: true });
    return val;
}

export default {
    props: {
        name: String
    },
    setup(props) {
        return {
            svg: asyncToRef(() => import('./' + (props.name ?? '') + '.svg')),
        }
    }
}
</script>
