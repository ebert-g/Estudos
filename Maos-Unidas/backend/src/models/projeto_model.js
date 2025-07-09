// Chamada do mongoose = banco de dados
const { Double } = require("bson");
const { Domain } = require("domain");
const mongoose = require("mongoose");
const { type } = require("os");
const { long, boolean } = require("webidl-conversions");
// Chamada da variavel Schema
const Schema = mongoose.Schema;

const Projeto = new Schema({
    id: {
        type:long,
        type: mongoose.Schema.Types.ObjectId,
        auto: true
    }, 
    titulo: {
        type: String,
        required: true
    },
    valorArrecadado: {
        type: Double,
    },
    dataCriacao: { 
        type: Date, 
        default: Date.now 
    },
    dataFinalizacao: { 
        type: Date, 
        default: Date.now 
    },
    status: {
        type: String,
        enum: ['Ativo', 'Inativo']
    }
})
mongoose.model("projeto", Projeto)