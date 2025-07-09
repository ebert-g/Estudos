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
    doador: {
        type: Schema.Types.ObjectId,
        ref: "usuario",
    },
    projeto: {
        type: Schema.Types.ObjectId,
        ref: "projeto",
    },
    valor: { 
        type: Double
    },
    data: { 
        type: Date, 
        default: Date.now 
    }
})
mongoose.model("projeto", Projeto)