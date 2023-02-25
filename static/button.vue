<template>
    <button type="button" @click="onClick">myButton</button>
</template>
<script>
export default {
    methods: {
        onClick() {
            console.log("button click");
            alert("click");
            example.test.myfunction("test", 1, 1.0);
        }
    }
}
</script>
