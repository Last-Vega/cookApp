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

      <v-text-field
      label="画像があったら教えてね"
      >
      </v-text-field>

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
      category: ''
    }
  }
}
</script>
