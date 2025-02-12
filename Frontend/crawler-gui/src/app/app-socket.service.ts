import { Injectable } from "@angular/core";
import { Socket } from "ngx-socket-io";
import { SOCKET_IO_CONFIG } from "./socket-config";

@Injectable({
    providedIn: 'root'
})
export class SocketService extends Socket {

    constructor() {
        super(SOCKET_IO_CONFIG)
    }
}