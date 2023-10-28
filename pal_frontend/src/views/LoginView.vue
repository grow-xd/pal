<template>
    <div
        class="relative flex min-h-screen text-gray-800 antialiased flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
        <div class="relative py-3 sm:w-96 mx-auto text-center">
            <span class="text-2xl font-light ">Login to your account</span>
            <div class="mt-4 bg-white shadow-md rounded-lg text-left">
                <div class="h-2 bg-purple-400 rounded-t-md"></div>
                <div class="px-8 py-6 ">
                    <label class="block font-semibold"> Username</label>
                    <input type="text" v-model="username" placeholder="Username"
                        class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
                    {{ username }}
                    <label class="block mt-3 font-semibold"> Password</label>
                    <input type="password" v-model="password" placeholder="Password"
                        class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
                    {{ password }}
                    <div class="flex justify-between items-baseline">
                        <button type="submit" @click="submit"
                            class="mt-4 bg-purple-500 text-white py-2 px-6 rounded-md hover:bg-purple-600 ">Login</button>
                        <a href="#" class="text-sm hover:underline">Forgot password?</a>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>

import { useToast } from "vue-toastification";

export default {
    setup() {
        // Get toast interface
        const toast = useToast();

        // Use it!


        // or with options

        // These options will override the options defined in the "app.use" plugin registration for this specific toast

        // Make it available inside methods
        return { toast }
    },
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        submit(e) {
            console.log(this.username)
            console.log(this.password)
            e.preventDefault();

            if (!this.username.length) {
                alert("enter username")
            }

            if (!this.password.length) {
                alert("enter password")
            }

            const requestOptions = {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({ username: this.username, password: this.password })


            }

            fetch('http://localhost:8000/api/login/', requestOptions)
                .then(result => result.json())
                .then(response => {
                    console.log(response)
                    if (response.status === 200) {
                        this.toast.success("Logged in");
                        console.log(response)
                        localStorage.setItem('token', response.access_token)

                    }
                    else {
                        this.toast.error(response.detail);

                    }
                    setTimeout(() => {
                        window.location.href = '/home'
                    }, 2000)

                })
        }
    }
}

</script>