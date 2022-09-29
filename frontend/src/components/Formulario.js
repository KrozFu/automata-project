import React, { useState } from 'react'

const Formulario = () => {

    const [datos, setDatos] = useState();

    return (
        <form role="form">
            <div className="form-group">
                <h1>Operacion con Automata</h1>
                <select className="form-control" id="" name="">
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
            <h2>First Automa Json</h2>
            <div className="form-group">
                <input className="btn btn-secondary" type="file" id="automata_one" />
            </div>
            <h2>Second Automata Json</h2>
            <div className="form-group">
                <input className="btn btn-secondary" type="file" id="automata_two" />
            </div>
            <button type="submit" className="btn btn-primary">Cargar Archivo</button>
        </form>
    );
}

export default Formulario;