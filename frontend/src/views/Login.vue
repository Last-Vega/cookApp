<template>
  <v-app>
    <v-card>
      <v-card-title>
        ユーザー情報を入力してください
      </v-card-title>
      <v-card-text>
        <v-text-field
          v-model="user.eMail"
          label="メールアドレス"
          >
        </v-text-field>
        <br />
        <v-text-field
          type="password"
          append-icon="mdi-eye-off"
          v-model="user.password"
          label="パスワード"
          >
        </v-text-field>
        <br />

      </v-card-text>
      <v-card-actions>
        <v-btn text v-on:click="canLogin">
          ログイン
        </v-btn>

      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>

export default {
  name: 'Register',

  components: {

  },

  data: function () {
    return {
      user: {
        eMial: '',
        password: ''
      },
      validationMessage: {
        aboutPassword: ''
      }
    }
  },
  methods: {
    async canLogin () {
      var regObj = new RegExp(/^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]{1,}\.[A-Za-z0-9]{1,}$/, 'g')
      var result = this.user.eMail.match(regObj)

      if (!this.user.eMail) {
        alert('メールアドレスを入力してください')
      } else if (!this.user.password) {
        alert('パスワードを入力してください')
      } else if (!result) {
        alert('不正なメールアドレスです')
      }

      const path = process.env.VUE_APP_BASE_URL + 'api/login'
      const self = this
      // パスワードのハッシュ化
      const uint8 = new TextEncoder().encode(this.user.password)
      const digest = await crypto.subtle.digest('SHA-256', uint8)
      const hashPassword = Array.from(new Uint8Array(digest))
        .map(v => v.toString(16).padStart(2, '0'))
        .join('')
      const params = new URLSearchParams()
      params.append('email', self.user.eMail)
      params.append('password', hashPassword)
      console.log(hashPassword)
      this.$api
        .post(path, params)
        .then(response => {
          if (response.data === 'permission denied') {
            alert('メールアドレスかパスワードが間違っています。')
            self.password = ''
          } else {
            // self.$store.commit('loginUser', response.data)
            this.$router.push('/')
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
