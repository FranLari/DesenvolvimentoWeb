<template>
  <ul>
    <li v-for="disciplina of disciplinas" v-bind:key="disciplina">
    {{disciplina.nome}} - {{disciplina.UNID1}} - {{disciplina.UNID2}} - {{disciplina.Media}} - {{disciplina.situacao}}
    </li>
  </ul>
</template>

<script>
export default {
  name: 'App',
  data(){
    return{
      disciplinas:[{nome:'Matemática Aplicada', UNID1:'7',UNID2:'7', Media:'7',situacao:'Aprovado'},
      {nome:'Banco de Dados', UNID1:'7',UNID2:'8', Media:'7.5',situacao:'Aprovado'}]

    }
  }
}
</script>

<style>

</style>
