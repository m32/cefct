<template>
    <main class="clock-main">
        <div class="clock-box">
            <svg
                style="clock-box"
                xmlns="http://www.w3.org/2000/svg"
                width="300"
                height="200"
                viewBox="0 0 600 600"
            >
                <g ref="face">
                    <circle class="clock-circle" cx="300" cy="300" r="253.9" />
                    <path
                        class="clock-hour-marks"
                        d="M300.5 94V61M506 300.5h32M300.5 506v33M94 300.5H60M411.3 107.8l7.9-13.8M493 190.2l13-7.4M492.1 411.4l16.5 9.5M411 492.3l8.9 15.3M189 492.3l-9.2 15.9M107.7 411L93 419.5M107.5 189.3l-17.1-9.9M188.1 108.2l-9-15.6"
                    />
                    <circle
                        class="clock-mid-circle"
                        cx="300"
                        cy="300"
                        r="16.2"
                    />
                </g>
                <g ref="hour" class="clock-hour">
                    <path class="clock-hour-arm" d="M300.5 298V142" />
                    <circle
                        class="clock-sizing-box"
                        cx="300"
                        cy="300"
                        r="253.9"
                    />
                </g>
                <g ref="minute" class="clock-minute">
                    <path class="clock-minute-arm" d="M300.5 298V67" />
                    <circle
                        class="clock-sizing-box"
                        cx="300"
                        cy="300"
                        r="253.9"
                    />
                </g>
                <g ref="second" class="clock-second">
                    <path class="clock-second-arm" d="M300.5 350V55" />
                    <circle
                        class="clock-sizing-box"
                        cx="300"
                        cy="300"
                        r="253.9"
                    />
                </g>
            </svg>
        </div>
    </main>
</template>
<script>
export default {
    data() {
        const date = new Date();
        let hr = date.getHours();
        let min = date.getMinutes();
        let sec = date.getSeconds();
        return {
            hrPosition: (hr * 360) / 12 + (min * (360 / 60)) / 12,
            minPosition: (min * 360) / 60 + (sec * (360 / 60)) / 60,
            secPosition: (sec * 360) / 60,
            tid: 0
        };
    },
    mounted() {
        this.tid = setInterval(this.runClock, 1000);
    },
    beforeUnmount() {
        clearInterval(this.tid);
    },
    methods: {
        runClock() {
            this.hrPosition += 3 / 360;
            this.minPosition += 6 / 60;
            this.secPosition += 6;

            this.$refs.hour.style.transform =
                'rotate(' + this.hrPosition + 'deg)';
            this.$refs.minute.style.transform =
                'rotate(' + this.minPosition + 'deg)';
            this.$refs.second.style.transform =
                'rotate(' + this.secPosition + 'deg)';
        }
    }
};
</script>
<style scoped>
.clock-main {
    display: flex;
    padding: 1em;
    height: 80vh;
    justify-content: center;
    align-items: middle;
}

.clock-box {
    width: 100%;
    height: 100%;
}

/* Clock styles */
.clock-circle {
    fill: none;
    stroke: #000;
    stroke-width: 9;
    stroke-miterlimit: 10;
}

.clock-mid-circle {
    fill: #000;
}

.clock-hour-marks {
    fill: none;
    stroke: #000;
    stroke-width: 9;
    stroke-miterlimit: 10;
}

.clock-hour-arm {
    fill: none;
    stroke: #000;
    stroke-width: 17;
    stroke-miterlimit: 10;
}

.clock-minute-arm {
    fill: none;
    stroke: #000;
    stroke-width: 11;
    stroke-miterlimit: 10;
}

.clock-second-arm {
    fill: none;
    stroke: #000;
    stroke-width: 4;
    stroke-miterlimit: 10;
}

/* Transparent box ensuring arms center properly. */
.clock-sizing-box {
    fill: none;
}

/* Make all arms rotate around the same center point. */
/* Optional: Use transition for animation. */
.clock-hour,
.clock-minute,
.clock-second {
    transform-origin: 300px 300px;
    transition: transform 0.5s ease-in-out;
}
</style>
