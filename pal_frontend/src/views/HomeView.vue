<template>
    <div class="bg-white space-y-10 justify-center">
        <div class="text-3xl text-center mt-12 m-6">
            Welcome, {{ name }}
        </div>

        <div class="bg-gray-300 p-10 space-y-7">
            <div class="text-2xl ml-20">Friends in your Area: {{ friends.length }}</div>
            <div class="text-2xl ml-20">Communities in your Area: {{ friends.length }}</div>

            <div class="text-2xl ml-20 font-bold pl-10">Scheduled Meetups:</div>
            <div class="flex justify-between bg-white ml-20 rounded-lg p-10">
                <div class="text-black text-xl ml-20">HTM Meetup</div>
                <div class="text-black text-xl ml-20">29/10/2023</div>
            </div>
        </div>

        <div class="text-3xl font-bold p-10 ml-20 text-center">Your friends in this area</div>

        <div class="flex overflow-y m-4">
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">Rishabh Gupta</div>
                <div class="text-lg text-black">@Rishabh</div>

                <div class="text-xl text-black mt-5">Available till : 11/11/2023</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">Rishabh Gupta</div>
                <div class="text-lg text-black">@Rishabh</div>

                <div class="text-xl text-black mt-5">Available till : 11/11/2023</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">Rishabh Gupta</div>
                <div class="text-lg text-black">@Rishabh</div>

                <div class="text-xl text-black mt-5">Available till : 11/11/2023</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">Rishabh Gupta</div>
                <div class="text-lg text-black">@Rishabh</div>

                <div class="text-xl text-black mt-5">Available till : 11/11/2023</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">Rishabh Gupta</div>
                <div class="text-lg text-black">@Rishabh</div>

                <div class="text-xl text-black mt-5">Available till : 11/11/2023</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">Rishabh Gupta</div>
                <div class="text-lg text-black">@Rishabh</div>

                <div class="text-xl text-black mt-5">Available till : 11/11/2023</div>
            </div>
        </div>


        <div class="text-3xl font-bold p-10 ml-20 text-center">Community Members in this area</div>

        <div class="flex overflow-y m-4">
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">HTM Community</div>
                <div class="text-lg text-black">@htm</div>

                <div class="text-xl text-black mt-5">Members available: 5</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">HTM Community</div>
                <div class="text-lg text-black">@htm</div>

                <div class="text-xl text-black mt-5">Members available: 5</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">HTM Community</div>
                <div class="text-lg text-black">@htm</div>

                <div class="text-xl text-black mt-5">Members available: 5</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">HTM Community</div>
                <div class="text-lg text-black">@htm</div>

                <div class="text-xl text-black mt-5">Members available: 5</div>
            </div>
            <div class="p-5 flex flex-col bg-gray-200 justify-center shadow-xl rounded-xl ml-20 m-6 space-y-3">
                <div class="text-2xl text-black">HTM Community</div>
                <div class="text-lg text-black">@htm</div>

                <div class="text-xl text-black mt-5">Members available: 5</div>
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