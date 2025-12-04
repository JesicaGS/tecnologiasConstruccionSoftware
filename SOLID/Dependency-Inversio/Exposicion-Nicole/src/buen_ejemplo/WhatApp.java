package buen_ejemplo;

public class WhatApp implements Notificador {
    @Override
    public void enviar(String mensaje) {
        System.out.println("Enviando Whastapp " + mensaje);
    }
}
