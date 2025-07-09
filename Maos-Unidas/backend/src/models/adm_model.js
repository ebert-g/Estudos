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
     usuario: {
         type: Schema.Types.ObjectId,
         ref: "usuario",
     },
     eAdm: {
        type: Number,
	    default: 0 // 1 é adm ou 0 e usuario comum  
    },
 })
 mongoose.model("projeto", Projeto)