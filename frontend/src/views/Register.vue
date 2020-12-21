<template>
  <v-app>
    <v-card>
      <v-card-title>
        ユーザー情報を入力してください
      </v-card-title>
      <v-card-text>
        <v-text-field
          v-model="user.user_name"
          label="ユーザー名"
          >
        </v-text-field>
        <br />
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
        <v-text-field
          type="password"
          append-icon="mdi-eye-off"
          v-model="user.Repassword"
          label="パスワード再入力"
          >
        </v-text-field>
        <br />
        <!-- ERRORS -->
        <div v-if="this.user.password !== this.user.Repassword">
          <h4>*入力されたパスワードが一致しません</h4>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn text v-on:click="canPost">
          登録する
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
        user_name: '',
        eMial: '',
        password: '',
        Repassword: ''
      },
      validationMessage: {
        aboutPassword: ''
      }
    }
  },
  methods: {
    async canPost () {
      var regObj = new RegExp(/^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]{1,}\.[A-Za-z0-9]{1,}$/, 'g')
      var result = this.user.eMail.match(regObj)

      if (!this.user.user_name) {
        alert('ユーザー名を入力してください')
      } else if (!this.user.eMail) {
        alert('メールアドレスを入力してください')
      } else if (!this.user.password) {
        alert('パスワードを入力してください')
      } else if (!this.user.Repassword) {
        alert('パスワードを再入力してください')
      } else if (this.user.password !== this.user.Repassword) {
        alert('入力されたパスワードが一致しません')
      } else if (!result) {
        alert('不正なメールアドレスです')
      } else {
        const path = process.env.VUE_APP_BASE_URL + 'api/registration'
        const self = this
        // パスワードのハッシュ化
        const uint8 = new TextEncoder().encode(this.user.password)
        const digest = await crypto.subtle.digest('SHA-256', uint8)
        const hashPassword = Array.from(new Uint8Array(digest))
          .map(v => v.toString(16).padStart(2, '0'))
          .join('')
        const params = new URLSearchParams()
        params.append('name', self.user.user_name)
        params.append('email', self.user.eMail)
        params.append('password', hashPassword)

        this.$api
          .post(path, params)
          .catch(error => {
            console.log(error)
          })

        this.$router.push('/login')
      }
    }
  }
}
</script>
