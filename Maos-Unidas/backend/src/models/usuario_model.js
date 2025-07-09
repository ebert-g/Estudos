// Chamada do mongoose = banco de dados
const mongoose = require("mongoose");
const { type } = require("os");
const { long, boolean } = require("webidl-conversions");
// Chamada da variavel Schema
const Schema = mongoose.Schema;

const Usuario = new Schema({
    id: {
        type:long,
        type: mongoose.Schema.Types.ObjectId,
        auto: true
    }, 
    nome: {
        type: String,
        required: true
    },
    email: {
        type: String,
        unique: true,
        required: true
    },
    senha: {
        type: String,
        require: true
    },
    tipo: {
        type: String,
        enum: ['ONG', 'DOADOR', 'EMPRESA'],
        required: true
    },
    fotoPerfil: {
        type: String,
        required: true
    },
    dataCadastro: { 
        type: Date, 
        default: Date.now 
    },
    status: {
        type: boolean
    }  
})
mongoose.model("usuario", Usuario)