import React, { Fragment, useState } from 'react'

const Formulario = () => {

    const [datos, setDatos] = useState();


    return (
        <form role="form">
            <div class="form-group">
                <h1>Operacion con Automata</h1>
                <select class="form-control" id="" name="">
                    <option value="Union">
                        Union
                    </option>
                    <option value="Interseccion">
                        Interseccion
                    </option>
                    <option value="Reverso">
                        Reverso
                    </option>
                    <option value="Complemento">
                        Complemento
                    </option>
                </select>
            </div>
            <h1>Primer Automata</h1>
            <div class="form-group">
                <input class="btn btn-secondary" type="file" id="ejemplo_archivo_1" />
            </div>
            <button type="submit" class="btn btn-primary">Cargar Automata</button>
        </form>
    );
}

export default Formulario;