<template>
  <div id="app">
    <!-- Sidebar -->
    <div id="sidebar" :class="{'active': isSidebarActive}">
      <div class="sidebar-header">
        <h3>Menu</h3>
        <button class="btn btn-outline-light btn-sm" @click="toggleSidebar">Fechar</button>
      </div>
      <ul class="list-unstyled components">
        <li>
          <router-link to="/">Cálculo de Área</router-link>
        </li>
        <li>
          <router-link to="/projetos">Projetos</router-link>
        </li>
        <li>
          <router-link to="/contato">Contato</router-link>
        </li>
      </ul>
    </div>

    <!-- Content -->
    <div id="content">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button type="button" id="sidebarCollapse" class="btn btn-info" @click="toggleSidebar">
          <i class="fas fa-align-left"></i>
          <span>Toggle Sidebar</span>
        </button>
      </nav>
      <div class="container-fluid">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isSidebarActive: false
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarActive = !this.isSidebarActive;
    }
  }
};
</script>

<style scoped>
/* Sidebar */
#sidebar {
  position: fixed;
  top: 0;
  left: -250px;
  width: 250px;
  height: 100vh;
  background: #343a40;
  color: #fff;
  transition: all 0.3s;
}

#sidebar.active {
  left: 0;
}

.sidebar-header {
  padding: 20px;
  background: #6c757d;
}

#sidebar ul.components {
  padding: 20px 0;
}

#sidebar ul li {
  padding: 10px;
  font-size: 1.1em;
}

#sidebar ul li a {
  color: #ddd;
  text-decoration: none;
}

#sidebar ul li a:hover {
  color: #fff;
  background: #007bff;
}

/* Content */
#content {
  width: 100%;
  padding: 20px;
  min-height: 100vh;
  transition: all 0.3s;
  margin-left: 0;
}

#sidebarCollapse {
  margin-left: 15px;
}

#sidebar.active + #content {
  margin-left: 250px;
}
</style>
