<template>
  <div class="signup">
    <!-- Username -->
    <div class="">
      <label for="username">Utilisateur</label>
      <input type="text" name="username" v-model="username" placeholder="Nom d'utilisateur">
    </div>


    <!-- Email -->
    <div class="">
      <label for="email">Email</label>
      <input type="email" name="email" v-model="email" placeholder="john.smith@gmail.com">
    </div>


    <!-- Password -->
    <div class="">
      <label for="password">Mot de passe</label>
      <input type="password" name="password" v-model="password" placeholder="Mot de passe">
    </div>


    <button @click="submitForm">S'enregistrer</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: () => {
    return {
      email: '',
      username: '',
      password: '',
    }
  },
  methods: {
    submitForm: function () {
      const formData = {username: this.username, email: this.email, password: this.password}

      axios
      .post("auth/users/", formData)
      .then(response => {
        console.log(response)
        this.$router.push("/login")
      })
      .catch(error => {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }

          console.log(JSON.stringify(error.response.data))

        } else if (error.message) {
          console.log(JSON.stringify(error.message))
        } else {
          console.log(JSON.stringify(error))
        }
      })
    }
  }
}
</script>
