<template>
    <button v-if="isLoggedIn=true" @click="logout" class="text-5xl text-emerald-800 text-center p-9">Log Out</button>
</template>

<script>

    export default {
        data() {
            isLoggedIn : false
        },
        created(){
            if(localStorage.getItem('token')){
                this.isLoggedIn=true
            }
        },
        methods: {
            logout(){
                localStorage.removeItem('token')
                window.location.href='/login'
            }
        }
    }

</script>