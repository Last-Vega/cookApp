<template>
  <v-app>
    <v-card>
      <v-card-title>
        おしゃんなアイテムを記録しよう
      </v-card-title>

      <v-text-field
      label="アイテムの名前を教えてね"
      >
      </v-text-field>

      <v-select
       outlined
       v-model="category"
       :items="items"
       item-text="label"
       item-value="value"
       label="カテゴリを教えてね"
       return-object
     ></v-select>

     <v-file-input
     label="アイテムの画像を選択してね"
     accept="image/*"
     filled
     prepend-icon="mdi-camera"
     show-size
     v-model="input_image"
     @change="onImagePicked"
    ></v-file-input>

    <img v-if="uploadImageUrl" :src="uploadImageUrl" width="30%" />

    </v-card>
  </v-app>
</template>

<script>
export default {
  name: 'Question',
  data () {
    return {
      items: [
        { label: 'Tシャツ' },
        { label: 'ロンティー' },
        { label: 'シャツ' },
        { label: 'スウェット' },
        { label: 'パーカー' },
        { label: 'アウター' },
        { label: 'パンツ' },
        { label: '香水' }
      ],
      category: '',
      input_image: null,
      uploadImageUrl: ''
    }
  },
  methods: {
    onImagePicked (file) {
      if (file !== undefined && file !== null) {
        if (file.name.lastIndexOf('.') <= 0) {
          return
        }
        const fr = new FileReader()
        fr.readAsDataURL(file)
        fr.addEventListener('load', () => {
          this.uploadImageUrl = fr.result
        })
      } else {
        this.uploadImageUrl = ''
      }
    }
  }
}
</script>
