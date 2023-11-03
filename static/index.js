class Indice {
  constructor() {
    this.clave = null;
    this.direccion = null;
  }

  update_data(clave, direccion) {
    this.clave = clave;
    this.direccion = direccion;
  }

  get_clave() {
    return this.clave;
  }

  get_direccion() {
    return this.direccion;
  }

  lt(otro) {
    if (this.clave === null || this.clave < 0) {
      return 1;
    }
    if (otro.clave === null || otro.clave < 0) {
      return -1;
    }
    return this.clave - otro.clave;
  }
}

class Dato {
  constructor(clave = null, nombre = "", apellido = "") {
    this.clave = clave;
    this.nombre = nombre;
    this.apellido = apellido;
  }

  update_data(clave, nombre = "", apellido = "") {
    this.clave = clave;
    this.nombre = nombre;
    this.apellido = apellido;
  }

  get_clave() {
    return this.clave;
  }

  get_nombre() {
    return this.nombre;
  }

  get_apellido() {
    return this.apellido;
  }

  lt(otro) {
    if (this.clave === null || this.clave < 0) {
      return 1;
    }
    if (otro.clave === null || otro.clave < 0) {
      return -1;
    }
    return this.clave - otro.clave;
  }
}

class Indice_Primario {
  constructor(cap_bloque, cant_registros, long_registro, long_indice) {
    this.cap_bloque = cap_bloque;
    this.cant_registros = cant_registros;
    this.long_registro = long_registro;
    this.long_indice = long_indice;
    this.reg_insertados = 0;
    this.estructura = new Array(cant_registros)
      .fill(null)
      .map(() => new Dato());
    this.est_indices = new Array(this.get_bloques_necesarios())
      .fill(null)
      .map(() => new Indice());
    this.actualizar_indices();
  }

  get_registros_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_registro);
  }

  get_bloques_necesarios() {
    return Math.ceil(this.cant_registros / this.get_registros_por_bloque());
  }

  get_reg_indice_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_indice);
  }

  get_bloques_indice_necesarios() {
    return Math.ceil(
      this.get_bloques_necesarios() / this.get_reg_indice_por_bloque()
    );
  }

  actualizar_indices() {
    let aux = 0;
    for (
      let i = 0;
      i < this.estructura.length;
      i += this.get_registros_por_bloque()
    ) {
      this.est_indices[aux].update_data(this.estructura[i].clave, i + 1);
      aux += 1;
    }
  }

  buscar_pos(clave) {
    for (let i = 0; i < this.reg_insertados; i++) {
      if (this.estructura[i].clave === clave) {
        return i;
      }
    }
    return -1;
  }

  isEmpty() {
    return this.estructura[0] === null;
  }

  insertar(clave, nombre = "", apellido = "") {
    if (this.reg_insertados < this.cant_registros) {
      for (let i = 0; i < this.reg_insertados; i++) {
        if (this.estructura[i].clave == clave) {
          return "La clave ya se encuentra en la estructura de datos";
        }
      }
      this.estructura[this.reg_insertados].update_data(clave, nombre, apellido);
      this.reg_insertados += 1;
      this.estructura.sort((a, b) => a.lt(b));
      this.actualizar_indices();
      let pos = this.buscar_pos(clave);
      return `El elemento se ha insertado correctamente en la posición ${
        (pos % this.get_registros_por_bloque()) + 1
      } del bloque que apunta al índice ${
        Math.floor(pos / this.get_registros_por_bloque()) + 1
      }`;
    } else {
      return "No se ha podido insertar el elemento debido a que la estructura está llena";
    }
  }

  eliminar(clave) {
    if (!this.isEmpty()) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }
      this.estructura[pos] = new Dato();
      this.reg_insertados -= 1;
      this.estructura.sort((a, b) => a.lt(b));
      this.actualizar_indices();
      return "El elemento ha sido eliminado satisfactoriamente";
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  buscar(clave) {
    if (!this.isEmpty()) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }
      return `El elemento ${clave}, de nombre ${this.estructura[pos].nombre} ${
        this.estructura[pos].apellido
      }, se ha encontrado en la posición ${
        (pos % this.get_registros_por_bloque()) + 1
      } del bloque que apunta al índice ${
        Math.floor(pos / this.get_registros_por_bloque()) + 1
      }`;
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  showStructure() {
    const estructura = document.createElement("div");

    const datosTable = document.createElement("table");
    datosTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Nombre</th>
                <th>Apellido</th>
            </tr>
        `;

    this.estructura.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>${item.apellido || ""}</td>
            `;
      datosTable.appendChild(row);
    });

    const indicesTable = document.createElement("table");
    indicesTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Direccion</th>
            </tr>
        `;

    this.est_indices.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.direccion || ""}</td>
            `;
      indicesTable.appendChild(row);
    });

    estructura.appendChild(datosTable);
    estructura.appendChild(indicesTable);

    estDiv.innerHTML = estructura.innerHTML;
  }
}

class Indice_Secundario {
  constructor(cap_bloque, cant_registros, long_registro, long_indice) {
    this.cap_bloque = cap_bloque;
    this.cant_registros = cant_registros;
    this.long_registro = long_registro;
    this.long_indice = long_indice;
    this.reg_insertados = 0;
    this.estructura = new Array(cant_registros)
      .fill(null)
      .map(() => new Dato());
    this.est_indices = new Array(cant_registros)
      .fill(null)
      .map(() => new Indice());
    this.actualizar_indices();
  }

  get_registros_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_registro);
  }

  get_bloques_necesarios() {
    return Math.ceil(this.cant_registros / this.get_registros_por_bloque());
  }

  get_reg_indice_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_indice);
  }

  get_bloques_indice_necesarios() {
    return Math.ceil(this.cant_registros / this.get_reg_indice_por_bloque());
  }

  actualizar_indices() {
    for (let i = 0; i < this.estructura.length; i++) {
      this.est_indices[i].update_data(this.estructura[i].clave, i + 1);
    }
  }

  buscar_pos(clave) {
    for (let i = 0; i < this.reg_insertados; i++) {
      if (this.estructura[i].clave === clave) {
        return i;
      }
    }
    return -1;
  }

  isEmpty() {
    return this.estructura[0] === null;
  }

  insertar(clave, nombre = "", apellido = "") {
    if (this.estructura[this.cant_registros - 1].clave === null) {
      for (let i = 0; i < this.reg_insertados; i++) {
        if (this.estructura[i].clave === clave) {
          return "La clave ya se encuentra en la estructura de datos";
        }
      }
      this.estructura[this.reg_insertados].update_data(clave, nombre, apellido);
      this.reg_insertados += 1;
      this.estructura.sort((a, b) => a.lt(b));
      this.actualizar_indices();
      let pos = this.buscar_pos(clave);
      return `El elemento se ha insertado correctamente en la posición ${
        pos + 1
      } del bloque que apunta al índice ${pos + 1}`;
    } else {
      return "No se ha podido insertar el elemento debido a que la estructura está llena";
    }
  }

  eliminar(clave) {
    if (!this.isEmpty()) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }
      this.estructura[pos] = new Dato();
      this.reg_insertados -= 1;
      this.estructura.sort((a, b) => a.lt(b));
      this.actualizar_indices();
      return "El elemento ha sido eliminado satisfactoriamente";
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  buscar(clave) {
    if (this.estructura[0] !== null) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }
      return `El elemento ${clave}, de nombre ${this.estructura[pos].nombre} ${
        this.estructura[pos].apellido
      }, se ha encontrado en la posición ${
        pos + 1
      } del bloque que apunta al índice ${pos + 1}`;
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  showStructure() {
    const estructura = document.createElement("div");

    const datosTable = document.createElement("table");
    datosTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Nombre</th>
                <th>Apellido</th>
            </tr>
        `;

    this.estructura.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>${item.apellido || ""}</td>
            `;
      datosTable.appendChild(row);
    });

    const indicesTable = document.createElement("table");
    indicesTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Direccion</th>
            </tr>
        `;

    this.est_indices.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.direccion || ""}</td>
            `;
      indicesTable.appendChild(row);
    });

    estructura.appendChild(datosTable);
    estructura.appendChild(indicesTable);

    estDiv.innerHTML = estructura.innerHTML;
  }
}

class Indice_Primario_Multinivel {
  constructor(cap_bloque, cant_registros, long_registro, long_indice) {
    this.cap_bloque = cap_bloque;
    this.cant_registros = cant_registros;
    this.long_registro = long_registro;
    this.long_indice = long_indice;
    this.reg_insertados = 0;
    this.estructura = new Array(
      Math.ceil(
        Math.log(this.get_bloques_necesarios()) / Math.log(this.get_reg_indice_por_bloque())
        ) + 1
      ).fill(null);
    this.estructura[0] = new Array(cant_registros)
      .fill(null)
      .map(() => new Dato());

    if (cant_registros !== 1) {
      this.estructura[1] = new Array(this.get_bloques_necesarios())
        .fill(null)
        .map(() => new Indice());

      if (this.get_bloques_indice_necesarios() > 1) {
        let aux = this.get_bloques_necesarios();
        for (let i = 2; i < this.estructura.length; i++) {
          this.estructura[i] = new Array(
            Math.ceil(aux / this.get_reg_indice_por_bloque())
          )
            .fill(null)
            .map(() => new Indice());
          aux = Math.ceil(aux / this.get_reg_indice_por_bloque());
        }
      }
    }

    this.actualizar_indices();
  }

  get_registros_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_registro);
  }

  get_bloques_necesarios() {
    return Math.ceil(this.cant_registros / this.get_registros_por_bloque());
  }

  get_reg_indice_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_indice);
  }

  get_bloques_indice_necesarios() {
    return Math.ceil(
      this.get_bloques_necesarios() / this.get_reg_indice_por_bloque()
    );
  }

  actualizar_indices() {
    if (this.cant_registros !== 1) {
      let aux = 0;
      for (
        let i = 0;
        i < this.cant_registros;
        i += this.get_registros_por_bloque()
      ) {
        this.estructura[1][aux].update_data(this.estructura[0][i].clave, i + 1);
        aux += 1;
      }

      if (this.estructura.length > 1) {
        for (let i = 2; i < this.estructura.length; i++) {
          aux = 0;
          for (
            let j = 0;
            j < this.estructura[i - 1].length;
            j += this.get_reg_indice_por_bloque()
          ) {
            this.estructura[i][aux].update_data(
              this.estructura[i - 1][j].clave,
              j + 1
            );
            aux += 1;
          }
        }
      }
    }
  }

  buscar_pos(clave) {
    for (let i = 0; i < this.reg_insertados; i++) {
      if (this.estructura[0][i].clave === clave) {
        return i;
      }
    }
    return -1;
  }

  isEmpty() {
    return this.estructura[0][0] === null;
  }

  insertar(clave, nombre = "", apellido = "") {
    if (this.estructura[0][this.cant_registros - 1].clave === null) {
      for (let i = 0; i < this.reg_insertados; i++) {
        if (this.estructura[0][i].clave === clave) {
          return "La clave ya se encuentra en la estructura de datos";
        }
      }

      this.estructura[0][this.reg_insertados].update_data(
        clave,
        nombre,
        apellido
      );
      this.reg_insertados += 1;
      this.estructura[0].sort((a, b) => a.lt(b));
      this.actualizar_indices();

      let pos = this.buscar_pos(clave);
      let aux = `El elemento ${clave} se ha insertado correctamente en la posición ${
        (pos % this.get_registros_por_bloque()) + 1
      } del nivel 0 de datos`;

      if (this.cant_registros !== 1) {
        aux += `, también en la posición ${
          (Math.floor(pos / this.get_registros_por_bloque()) %
            this.get_reg_indice_por_bloque()) +
          1
        } del nivel ${this.estructura.length - 1} de índices`;

        if (this.estructura.length > 1) {
          pos =
            Math.floor(
              (pos - this.get_registros_por_bloque()) /
                this.get_registros_por_bloque()
            ) + 1;

          for (let i = 2; i < this.estructura.length; i++) {
            aux += `, también en la posición ${
              Math.floor(pos / this.get_reg_indice_por_bloque()) + 1
            } del nivel ${this.estructura.length - i} de índices`;
            pos = Math.floor(pos / this.get_reg_indice_por_bloque()) + 1;
          }
        }
      }
      return aux;
    } else {
      return "No se ha podido insertar el elemento debido a que la estructura está llena";
    }
  }

  eliminar(clave) {
    if (!this.isEmpty) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }
      this.estructura[0][pos] = new Dato();
      this.reg_insertados -= 1;
      this.estructura[0].sort((a, b) => a.lt(b));
      this.actualizar_indices();
      return "El elemento ha sido eliminado satisfactoriamente";
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  buscar(clave) {
    if (!this.isEmpty) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }

      let aux = `El elemento ${clave} se ha encontrado satisfactoriamente en la posición ${
        (pos % this.get_registros_por_bloque()) + 1
      } del nivel 0 de datos`;

      if (this.cant_registros !== 1) {
        aux += `, también en la posición ${
          (Math.floor(pos / this.get_registros_por_bloque()) %
            this.get_reg_indice_por_bloque()) +
          1
        } del nivel ${this.estructura.length - 1} de índices`;

        if (this.estructura.length > 1) {
          pos =
            Math.floor(
              (pos - this.get_registros_por_bloque()) /
                this.get_registros_por_bloque()
            ) + 1;

          for (let i = 2; i < this.estructura.length; i++) {
            aux += `, también en la posición ${
              Math.floor(pos / this.get_reg_indice_por_bloque()) + 1
            } del nivel ${this.estructura.length - i} de índices`;
            pos = Math.floor(pos / this.get_reg_indice_por_bloque()) + 1;
          }
        }
      }
      return aux;
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  showStructure() {
    const estructura = document.createElement("div");

    const datosTable = document.createElement("table");
    datosTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Nombre</th>
                <th>Apellido</th>
            </tr>
        `;

    this.estructura[0].forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>${item.apellido || ""}</td>
            `;
      datosTable.appendChild(row);
    });

    estructura.appendChild(datosTable);

    if (this.cant_registros !== 1) {
      let indicesTable = document.createElement("table");
      indicesTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Direccion</th>
            </tr>
        `;

      this.estructura[1].forEach((item) => {
        const row = document.createElement("tr");
        row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.direccion || ""}</td>
            `;
        indicesTable.appendChild(row);
      });

      estructura.appendChild(indicesTable);

      if (this.get_bloques_indice_necesarios() > 1) {
        for (let i = 2; i < this.estructura.length; i++) {
          indicesTable = document.createElement("table");
          indicesTable.innerHTML = `
                  <tr>
                      <th>Clave</th>
                      <th>Direccion</th>
                  </tr>
              `;

          this.estructura[i].forEach((item) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                      <td>${item.clave || ""}</td>
                      <td>${item.direccion || ""}</td>
                  `;
            indicesTable.appendChild(row);
          });

          estructura.appendChild(indicesTable);
        }
      }
    }

    estDiv.innerHTML = estructura.innerHTML;
  }
}

class Indice_Secundario_Multinivel {
  constructor(cap_bloque, cant_registros, long_registro, long_indice) {
    
    this.cap_bloque = cap_bloque;
    this.cant_registros = cant_registros;
    this.long_registro = long_registro;
    this.long_indice = long_indice;
    this.reg_insertados = 0;
    this.estructura = new Array(
      Math.ceil(Math.log(cant_registros) / Math.log(this.get_reg_indice_por_bloque())) + 1
      ).fill(null);
    this.estructura[0] = new Array(cant_registros)
      .fill(null)
      .map(() => new Dato());

    if (cant_registros !== 1) {
      this.estructura[1] = new Array(cant_registros)
        .fill(null)
        .map(() => new Indice());

      if (this.get_bloques_indice_necesarios() > 1) {
        let aux = cant_registros;
        for (let i = 2; i < this.estructura.length; i++) {
          this.estructura[i] = new Array(
            Math.ceil(aux / this.get_reg_indice_por_bloque())
          )
            .fill(null)
            .map(() => new Indice());
          aux = Math.ceil(aux / this.get_reg_indice_por_bloque());
        }
      }
    }

    this.actualizar_indices();
  }

  get_registros_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_registro);
  }

  get_bloques_necesarios() {
    return Math.ceil(this.cant_registros / this.get_registros_por_bloque());
  }

  get_reg_indice_por_bloque() {
    return Math.floor(this.cap_bloque / this.long_indice);
  }

  get_bloques_indice_necesarios() {
    return Math.ceil(this.cant_registros / this.get_reg_indice_por_bloque());
  }

  actualizar_indices() {
    if (this.cant_registros !== 1) {
      let aux = 0;
      for (let i = 0; i < this.cant_registros; i += 1) {
        this.estructura[1][aux].update_data(this.estructura[0][i].clave, i + 1);
        aux += 1;
      }

      if (this.estructura.length > 1) {
        for (let i = 2; i < this.estructura.length; i++) {
          aux = 0;
          for (
            let j = 0;
            j < this.estructura[i - 1].length;
            j += this.get_reg_indice_por_bloque()
          ) {
            this.estructura[i][aux].update_data(
              this.estructura[i - 1][j].clave,
              j + 1
            );
            aux += 1;
          }
        }
      }
    }
  }

  buscar_pos(clave) {
    for (let i = 0; i < this.reg_insertados; i++) {
      if (this.estructura[0][i].clave === clave) {
        return i;
      }
    }
    return -1;
  }

  isEmpty() {
    return this.estructura[0][0] === null;
  }

  insertar(clave, nombre = "", apellido = "") {
    if (this.estructura[0][this.cant_registros - 1].clave === null) {
      for (let i = 0; i < this.reg_insertados; i++) {
        if (this.estructura[0][i].clave === clave) {
          return "La clave ya se encuentra en la estructura de datos";
        }
      }

      this.estructura[0][this.reg_insertados].update_data(
        clave,
        nombre,
        apellido
      );
      this.reg_insertados += 1;
      this.estructura[0].sort((a, b) => a.lt(b));
      this.actualizar_indices();

      let pos = this.buscar_pos(clave);
      let aux = `El elemento ${clave} se ha insertado correctamente en la posición ${
        (pos % this.get_registros_por_bloque()) + 1
      } del nivel 0 de datos`;

      if (this.cant_registros !== 1) {
        aux += `, también en la posición ${
          (Math.floor(pos / this.get_registros_por_bloque()) %
            this.get_reg_indice_por_bloque()) +
          1
        } del nivel ${this.estructura.length - 1} de índices`;

        if (this.estructura.length > 1) {
          pos =
            Math.floor(
              (pos - this.get_registros_por_bloque()) /
                this.get_registros_por_bloque()
            ) + 1;

          for (let i = 2; i < this.estructura.length; i++) {
            aux += `, también en la posición ${
              Math.floor(pos / this.get_reg_indice_por_bloque()) + 1
            } del nivel ${this.estructura.length - i} de índices`;
            pos = Math.floor(pos / this.get_reg_indice_por_bloque()) + 1;
          }
        }
      }
      return aux;
    } else {
      return "No se ha podido insertar el elemento debido a que la estructura está llena";
    }
  }

  eliminar(clave) {
    if (!this.isEmpty) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }

      this.estructura[0][pos] = new Dato();
      this.reg_insertados -= 1;
      this.estructura[0].sort((a, b) => a.lt(b));
      this.actualizar_indices();
      return "El elemento ha sido eliminado satisfactoriamente";
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  buscar(clave) {
    if (!this.isEmpty) {
      let pos = this.buscar_pos(clave);
      if (pos === -1) {
        return "El elemento no se encuentra en la estructura";
      }

      let aux = `El elemento ${clave} se ha encontrado satisfactoriamente en la posición ${
        (pos % this.get_registros_por_bloque()) + 1
      } del nivel 0 de datos`;

      if (this.cant_registros !== 1) {
        aux += `, también en la posición ${
          (Math.floor(pos / this.get_registros_por_bloque()) %
            this.get_reg_indice_por_bloque()) +
          1
        } del nivel ${this.estructura.length - 1} de índices`;

        if (this.estructura.length > 1) {
          pos =
            Math.floor(
              (pos - this.get_registros_por_bloque()) /
                this.get_registros_por_bloque()
            ) + 1;

          for (let i = 2; i < this.estructura.length; i++) {
            aux += `, también en la posición ${
              Math.floor(pos / this.get_reg_indice_por_bloque()) + 1
            } del nivel ${this.estructura.length - i} de índices`;
            pos = Math.floor(pos / this.get_reg_indice_por_bloque()) + 1;
          }
        }
      }
      return aux;
    } else {
      return "El elemento no se encuentra en la estructura";
    }
  }

  showStructure() {
    const estructura = document.createElement("div");

    const datosTable = document.createElement("table");
    datosTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Nombre</th>
                <th>Apellido</th>
            </tr>
        `;

    this.estructura[0].forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>${item.apellido || ""}</td>
            `;
      datosTable.appendChild(row);
    });

    estructura.appendChild(datosTable);

    if (this.cant_registros !== 1) {
      let indicesTable = document.createElement("table");
      indicesTable.innerHTML = `
            <tr>
                <th>Clave</th>
                <th>Direccion</th>
            </tr>
        `;

      this.estructura[1].forEach((item) => {
        const row = document.createElement("tr");
        row.innerHTML = `
                <td>${item.clave || ""}</td>
                <td>${item.direccion || ""}</td>
            `;
        indicesTable.appendChild(row);
      });

      estructura.appendChild(indicesTable);

      if (this.get_bloques_indice_necesarios() > 1) {
        for (let i = 2; i < this.estructura.length; i++) {
          indicesTable = document.createElement("table");
          indicesTable.innerHTML = `
                  <tr>
                      <th>Clave</th>
                      <th>Direccion</th>
                  </tr>
              `;

          this.estructura[i].forEach((item) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                      <td>${item.clave || ""}</td>
                      <td>${item.direccion || ""}</td>
                  `;
            indicesTable.appendChild(row);
          });

          estructura.appendChild(indicesTable);
        }
      }
    }

    estDiv.innerHTML = estructura.innerHTML;
  }
}

let indexType;

let cap_bloque,
  cant_registros,
  long_indice,
  long_registro,
  estructura,
  estDiv = document.getElementById("structure");

function create_structure() {
  cap_bloque = parseInt(
    document.getElementById("form-structure_capBloque").value
  );
  cant_registros = parseInt(
    document.getElementById("form-structure_cantRegistros").value
  );
  long_registro = parseInt(
    document.getElementById("form-structure_longRegistro").value
  );
  long_indice = parseInt(
    document.getElementById("form-structure_longIndice").value
  );
  if (cap_bloque && cant_registros && long_registro && long_indice) {
    switch (indexType) {
        case 1:
            estructura = new Indice_Primario(cap_bloque, cant_registros, long_registro, long_indice);
            document.getElementById("form-key").style.display = "flex";
            document.getElementById("structure").style.display = "flex";
            estructura.showStructure();
            break;
        case 2:
            estructura = new Indice_Secundario(cap_bloque, cant_registros, long_registro, long_indice);
            document.getElementById("form-key").style.display = "flex";
            document.getElementById("structure").style.display = "flex";
            estructura.showStructure();
            break;
        case 3:
            estructura = new Indice_Primario_Multinivel(cap_bloque, cant_registros, long_registro, long_indice);
            document.getElementById("form-key").style.display = "flex";
            document.getElementById("structure").style.display = "flex";
            estructura.showStructure();
            break;
        case 4:
            estructura = new Indice_Secundario_Multinivel(cap_bloque, cant_registros, long_registro, long_indice);
            document.getElementById("form-key").style.display = "flex";
            document.getElementById("structure").style.display = "flex";
            estructura.showStructure();
            break;
    }
    
  } else {
    alert("Todos los campos son obligatorios");
  }
}

let key, firstName, lastName;

function add_key() {
  key = document.getElementById("form-key_keyInput").value;
  firstName = document.getElementById("form-key_nameInput").value;
  lastName = document.getElementById("form-key_lastNameInput").value;
  if (key) {
    alert(estructura.insertar(key, firstName, lastName));
    estructura.showStructure();
  } else {
    alert("Inserte una clave");
  }
}

function delete_key() {
  key = document.getElementById("form-key_keyInput").value;
  if (key) {
    alert(estructura.eliminar(key));
    estructura.showStructure();
  } else {
    alert("Inserte una clave");
  }
}

function find_key() {
  key = document.getElementById("form-key_keyInput").value;
  if (key) {
    alert(estructura.buscar(key));
  } else {
    alert("Inserte una clave");
  }
}

let submitButton = document.getElementById("form-structure_submit");
submitButton.addEventListener("click", create_structure);

let addButton = document.getElementById("form-key_addKey");
addButton.addEventListener("click", add_key);

let findButton = document.getElementById("form-key_findKey");
findButton.addEventListener("click", find_key);

let deleteButton = document.getElementById("form-key_deleteKey");
deleteButton.addEventListener("click", delete_key);



function startIndexPrimaryOneLevel() {
    indexType = 1;
    document.getElementById("buttons").style.display = "none";
    document.getElementById("form-structure").style.display = "flex";
    document.getElementById("form-key").style.display = "hidden";
    document.getElementById("structure").style.display = "hidden";
}

function startIndexSecondaryOneLevel() {
    indexType = 2;
    document.getElementById("buttons").style.display = "none";
    document.getElementById("form-structure").style.display = "flex";
    document.getElementById("form-key").style.display = "hidden";
    document.getElementById("structure").style.display = "hidden";
}

function startIndexPrimaryMultipleLevels() {
    indexType = 3;
    document.getElementById("buttons").style.display = "none";
    document.getElementById("form-structure").style.display = "flex";
    document.getElementById("form-key").style.display = "hidden";
    document.getElementById("structure").style.display = "hidden";
}

function startIndexSecondaryMultipleLevels() {
    indexType = 4;
    document.getElementById("buttons").style.display = "none";
    document.getElementById("form-structure").style.display = "flex";
    document.getElementById("form-key").style.display = "hidden";
    document.getElementById("structure").style.display = "hidden";
}

document.getElementById("indexPrimary_oneLevel").addEventListener("click", startIndexPrimaryOneLevel);
document.getElementById("indexSecondary_oneLevel").addEventListener("click", startIndexSecondaryOneLevel);
document.getElementById("indexPrimary_multipleLevel").addEventListener("click", startIndexPrimaryMultipleLevels);
document.getElementById("indexSecondary_multipleLevel").addEventListener("click", startIndexSecondaryMultipleLevels);