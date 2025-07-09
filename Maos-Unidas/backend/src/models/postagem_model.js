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
    usuario: {
        type: Schema.Types.ObjectId,
        ref: "usuario",
    },
    titulo: {
        type: String,
        required: true
    },
    conteudo: {
        type: String,
        required: true
    },
    dataPublicacao: { 
        type: Date, 
        default: Date.now 
    }
})
mongoose.model("ong", Ong)