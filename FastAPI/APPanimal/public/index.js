
async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais')
    
    const animais = response.data

    const lista = document.getElementById("lista-animais")

    lista.innerHTML = ''

    animais.forEach(animal => {

        const item = document.createElement('li')
        const nome_and_id = `${animal.nome} - id:${animal.id}`
        item.innerText = nome_and_id
    
        lista.appendChild(item)
    })
}


function cadastrarAnimal() {
    const form_animal = document.getElementById("form-animal")
    const input_nome = document.getElementById("nome")
    const input_idade = document.getElementById("idade")
    const input_sexo = document.getElementById("sexo")
    const input_cor = document.getElementById("cor")


    //uma funcao java script que tem parametros e um corpo
    form_animal.onsubmit = async (event) => {
        //para não recarregar a página sempre que submeter
        event.preventDefault()

        //variaveis
        const nome_animal = input_nome.value
        const idade_animal = input_idade.value
        const sexo_animal = input_sexo.value
        const cor_animal = input_cor.value

        await axios.post('http://localhost:8000/animais', {
            nome: nome_animal,
            idade: idade_animal,
            sexo: sexo_animal,
            cor: cor_animal
        })

        carregarAnimais()
        alert(`${nome_animal} cadastrado com sucesso`)

    }
}



function deletarAnimais() {
    const form_deletar = document.getElementById('deletar')
    const input_id_deletar = document.getElementById('id-animal-deletar')

    form_deletar.onsubmit = async (event) => {
        event.preventDefault()
        const id_deletar = input_id_deletar.value

        await axios.delete(`http://localhost:8000/animais/${id_deletar}`)

        carregarAnimais()
        alert(`deletado com sucesso`)
    }
}

function buscarAnimal(){
    const form_buscar = document.getElementById("buscar-animal")
    const input_id_buscar = document.getElementById("id-buscar-animal")

    form_buscar.onsubmit = async (event) => {
        event.preventDefault()

        const id_buscar = input_id_buscar.value

        const resposta = await axios.get(`http://localhost:8000/animais/${id_buscar}`)

        animal_encontrado = resposta.data

        const lista_animais_buscados = document.getElementById("animal-encontrado")

        const li = document.createElement('li')

        const dados_animal = `${animal_encontrado.nome}
         idade:${animal_encontrado.idade}
         sexo:${animal_encontrado.sexo}
         cor:${animal_encontrado.cor}
        `
        li.innerText = dados_animal

        lista_animais_buscados.innerHTML = ''
        lista_animais_buscados.appendChild(li)

    }
}

function app() {
    console.log('App iniciado')
    carregarAnimais()
    cadastrarAnimal()
    deletarAnimais()
    buscarAnimal()
}

app()