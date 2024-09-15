<template>
  <div class="text-center">
    <h1 class="display-5">Cálculo de Área e Custo de Construção</h1>
    <div class="card p-4 shadow-sm mt-4">
      <form @submit.prevent="calculateAreaCost">
        <div class="mb-3">
          <label for="altura" class="form-label">Altura (m):</label>
          <input v-model="altura" type="number" id="altura" class="form-control" placeholder="Digite a altura" required />
        </div>
        <div class="mb-3">
          <label for="largura" class="form-label">Largura (m):</label>
          <input v-model="largura" type="number" id="largura" class="form-control" placeholder="Digite a largura" required />
        </div>
        <div class="mb-3">
          <label for="preco_por_metro" class="form-label">Preço por Metro (R$):</label>
          <input v-model="preco_por_metro" type="number" id="preco_por_metro" class="form-control" placeholder="Digite o preço por metro" required />
        </div>
        <button type="submit" class="btn btn-primary">Calcular</button>
      </form>

      <div v-if="resultado" class="mt-4">
        <h4>Resultados:</h4>
        <p><strong>Área:</strong> {{ resultado.area }} m²</p>
        <p><strong>Custo:</strong> R$ {{ resultado.custo }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      altura: null,
      largura: null,
      preco_por_metro: null,
      resultado: null
    };
  },
  methods: {
    async calculateAreaCost() {
      try {
        const response = await fetch("http://127.0.0.1:5000/calculo", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            altura: this.altura,
            largura: this.largura,
            preco_por_metro: this.preco_por_metro
          })
        });
        this.resultado = await response.json();
      } catch (error) {
        console.error("Erro ao calcular:", error);
      }
    }
  }
};
</script>

<style scoped>
.card {
  max-width: 600px;
  margin: auto;
}
h1 {
  color: navy;
  font-size: 2.5rem;
}
.form-control {
  padding: 0.75rem;
  font-size: 1rem;
}
button {
  font-size: 1.1rem;
}
</style>
