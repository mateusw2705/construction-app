import { createRouter, createWebHistory } from 'vue-router';
import CalculoArea from './components/CalculoArea.vue';
import PaginaProjetos from './components/PaginaProjetos.vue';
import PaginaContato from './components/PaginaContato.vue';

const routes = [
  { path: '/', component: CalculoArea },
  { path: '/projetos', component: PaginaProjetos },
  { path: '/contato', component: PaginaContato },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
