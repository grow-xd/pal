<template>
    <!-- component -->
    <div
        class="relative bg-[url(../assets/img3.jpg)] bg-center flex min-h-screen text-gray-800 antialiased flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
        <div class="relative py-3 sm:w-96 mx-auto text-center">
            <span class="text-2xl font-bold ">Create New Account</span>
            <div class="mt-4 bg-white shadow rounded-lg text-left">
                <div class="h-2 bg-purple-400 rounded-t-md"></div>
                <div class="px-8 py-6 ">
                    <label class="block font-semibold"> Full Name</label>
                    <input type="text" v-model="name" placeholder="Full Name"
                        class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
                    <!-- {{ name }} -->
                    <label class="block mt-3 font-semibold"> Username</label>
                    <input type="text" v-model="username" placeholder="Username"
                        class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
                    <!-- {{ username }} -->
                    <label class="block mt-3 font-semibold"> Password</label>
                    <input type="password" v-model="password" placeholder="Password"
                        class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
                    <!-- {{ password }} -->
                    <label class="block mt-3 font-semibold"> Current Location</label>
                    <input type="text" v-model="location" placeholder="Location"
                        class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
                    <!-- {{ location }} -->
                    <div class="flex justify-center items-baseline">
                        <button type="submit" @click="submit"
                            class="mt-4 bg-purple-500 text-white py-2 px-6  rounded-md hover:bg-purple-600 ">Signup</button>

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
        const toast = useToast();
        return { toast }
    },

    data() {
        return {
            name: '',
            username: '',
            password: '',
            location: '',
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

            if (!this.name.length) {
                alert("enter Name")
            }

            if (!this.location.length) {
                alert("enter Location")
            }

            const requestOptions = {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({ name: this.name, username: this.username, password: this.password, location: this.location })


            }

            fetch('http://localhost:8000/api/signup/', requestOptions)
                .then(result => result.json())
                .then(response => {
                    console.log(response)
                    if (response.status === 200) {
                        this.toast.success("Logged in");
                        console.log(response)
                        localStorage.setItem('token', response.access_token)

                    }
                    else {
                        this.toast.error(response);

                    }
                })

        }
    }
}

</script>