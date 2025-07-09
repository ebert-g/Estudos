// Chamada do mongoose = banco de dados
const mongoose = require("mongoose");
const { type } = require("os");
const { long, boolean } = require("webidl-conversions");
// Chamada da variavel Schema
const Schema = mongoose.Schema;

const Ong = new Schema({
    id: {
        type:long,
        type: mongoose.Schema.Types.ObjectId,
        auto: true
    }, 
    nome: {
        type: String,
        required: true
    },
    descricao: {
        type: String,
        required: true
    },
    categoria: {
        type: String,
        // tem que complementar
        enum: ['Educação', 'Saúde', 'Meio Ambiente'],
        required: true
    },
    site: {
        type: String,
        required: true
    },
    localizacao: {
        type: String,
        required: true
    },
    contato: {
        type: String,
        required: true
    },
    status: {
        type: boolean
    }  
})
mongoose.model("ong", Ong)