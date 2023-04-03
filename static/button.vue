<template>
    <button type="button" @click="onClick">myButton</button>
</template>
<script>
export default {
    methods: {
        onClick() {
            console.log("button click");
            let data = {
                'string': 'text',
                'int': 1,
                'float': 1.1
            };
            data = JSON.stringify(data);
            window.cefQuery({
                request: data,
                onSuccess: function(response) {
                    console.log("onSuccess:", response);
                },
                onFailure: function(error_code, error_message) {
                    console.log("onFailure:", error_code, error_message);
                },
                persistent: false,
            });
        }
    }
}
</script>
