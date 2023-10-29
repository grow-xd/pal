
<template>
    <div class="bg-blue-700 h-screen rounded-xl m-2">
        <div class="text-center text-7xl font-bold p-20 text-white">
            Welcome, {{ name }}
        </div>
        <div class="flex flex-cols justify-center">
            <div class="text-center text-2xl font-bold p-4 text-white">
                Your current location: {{ location }}
            </div>
            
        </div>

        <hr class="my-12 h-0.5 border-t-0 bg-neutral-100 opacity-100 dark:opacity-50 m-6 mt-20" />

        <div class="grid grid-cols-2 divide-x pt-6 ">


            <div class="col-span-1 min-h-screen items-center justify-center">

                <div class=" text-center text-2xl underline font-bold text-white p-4">
                    <br>
                    Friends in your area

                </div>

                <div class="flex justify-items-center justify-center m-2" v-for="friend in friends" v-bind:key="friend.id">

                    <div class="text-lg bg-white shadow-xl rounded-xl w-2/3 text-black p-2">
                        {{ friend.name }}
                        {{ friend.username }}
                        {{ friend.location }}
                    </div>


                </div>

            </div>

            <div class="col-span-1">
                <div class=" text-center text-2xl underline font-bold text-white p-4">
                    Communities members in your area
                </div>
                <div class="flex justify-items-center justify-center m-2">

                    <div class="flex justify-between text-lg bg-white shadow-xl rounded-xl w-2/3 text-black p-2">
                        <div class="text-lg font-bold">name</div>
                        <div class="text-lg">community</div>
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
            id: '',
            username: '',
            name: '',
            location: '',
            friends: [],
        }
    },
    created() {
        this.getInfo()

    },

    methods: {

        getInfo() {

            const token = localStorage.getItem('token')

            const requestOptions = {
                method: "GET",
                headers: {
                    "Content-type": "application/json",
                    'Authorization': `Bearer ${token}`
                }


            }

            fetch('http://localhost:8000/api/get_user_info/', requestOptions)
                .then(result => result.json())
                .then(response => {
                    console.log(response)

                    this.id = response.id
                    this.name = response.name
                    this.username = response.username
                    this.location = response.location

                    this.getfriends()


                })
        },

        getfriends() {

            const token = localStorage.getItem('token')

            const requestOptions = {
                method: "GET",
                headers: {
                    "Content-type": "application/json",
                    'Authorization': `Bearer ${token}`
                }


            }

            fetch(`http://localhost:8000/api/userprofiles/${this.id}/friends/${this.location}`, requestOptions)
                .then(result => result.json())
                .then(response => {

                    console.log(response)

                    this.friends = response

                })
        },

        
    }
}

</script>