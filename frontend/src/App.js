import Formulario from './components/Formulario';
import { useEffect, useState } from 'react';
import Graphviz from 'graphviz-react';
import axios, { Axios } from 'axios';
import './App.css';


function App() {
  // const [archivos, setArchivos] = useState(null);
  // const [automata, setListAutomatas] = useState([]);

  // const subirArchivos = e => {
  //   setArchivos(e);
  // }

  // const insertarArchivos = async () => {
  //   const f = new FormData();

  //   for (let index = 0; index < archivos.length; index++) {
  //     f.append("file", archivos[index]);
  //   }

  //   await axios.post("/upload", f)
  //     .then(response => {
  //       console.log(response.data);
  //     }).catch(error => {
  //       console.log(error);
  //     })
  // }

  // const cargar = () => {
  //   const cargarAutomata = async () => {
  //     const url = "/renderAutomata";
  //     const result = await axios.get(url);

  //     setListAutomatas(result.data)
  //   }
  //   // console.log(automata)
  //   cargarAutomata();
  // }

  // const GraphvizPage = () => {
  //   const dot = automata;
  //   console.log(dot);
  //   return <Graphviz dot={dot} />;
  // }


  // useEffect(cargar, []);


  return (
    <div className="App">
      <header className="App-header">

        <Formulario />

        {/* "proxy": "http://127.0.0.1:8000" */}

        {/* <h1>Segundo Automata</h1>
        <input class="btn btn-secondary" type="file" name="files" multiple onChange={(e) => subirArchivos(e.target.files)} />
        <br />
        <button class="btn btn-primary" onClick={() => insertarArchivos()}>
          Cargar Automatas
        </button> */}


        {/* <button type="button" onClick={() => grafito()}>
          Traer Automata
        </button> */}

        {/* <GraphvizPage /> */}

      </header>
    </div >
  );
}

export default App;