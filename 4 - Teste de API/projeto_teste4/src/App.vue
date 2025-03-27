<template>
  <div id="app">
    <h1>Busca Textual</h1>

    <div class="bloco">
    <input v-model="searchTerm" placeholder="Digite: Razão Social, CNPJ, Telefone ou Cidade" />
    <button @click="search">Buscar</button>
    </div>

    <div v-if="error" style="color: red;">
      Ocorreu um erro ao buscar os dados.
    </div>

    <table v-if="results.length > 0">
      <thead>
        <tr>
          <th>Razão Social</th>
          <th>CNPJ</th>
          <th>Telefone</th>
          <th>Cidade</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="result in results" :key="result.CNPJ">
          <td>{{ result.Razao_Social }}</td>
          <td>{{ result.CNPJ }}</td>
          <td>{{formatTelefone(result.Telefone_Completo)}}</td>
          <td>{{ result.Cidade }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchTerm: '',
      results: [],
      loading: false,
      error: false,
    };
  },
  methods: {
    async search() {
      if (this.searchTerm.length < 2) {
        alert('Digite ao menos 2 caracteres.');
        return;
      }

      try {
        const response = await fetch(`http://127.0.0.1:8000/buscar?termo=${this.searchTerm}`);
        const data = await response.json();
        this.results = data;
      } catch (err) {
        this.error = true;
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    formatTelefone(telefone) {
      return telefone && telefone.startsWith("0") ? telefone.slice(1) : telefone;
    }
  }
};
</script>

<style>
body{
  background-color: #d4def396;
}
h1 {
  text-align: center;
  font-family: 'Courier New', Courier, monospace;
  font-weight: normal;
}

.bloco{
  display: flex;              
  flex-direction: row;     
  justify-content: center;    
  align-items: center;
  
}

input {
  padding: 10px;
  font-size: 16px;
  margin: 10px;
  width: 35%;
  font-family: 'Courier New', Courier, monospace;
  font-weight: normal;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  font-family: 'Courier New', Courier, monospace;
  font-weight: normal;
}
button:hover {
  background-color: #0056b3;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  
}
th, td {
  padding: 12px;
  text-align: left;
  border: 1px solid #000000;
}
</style>
