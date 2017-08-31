import { mapGetters, mapActions } from 'vuex';
import { SET_MESSAGES } from '../../store/mutation-types'

export default {
    name: 'chat',
    computed: {
        ...mapGetters([
            'messages'
        ]),
    },
    methods: {
        ...mapActions([
            SET_MESSAGES
        ]),
        send_message() {
            // this.messages.push(this.message);
            this.SET_MESSAGES(this.message)
            this.message = "";
        }
    },
    data() {
        return {
            channels: ["general", "random"],
            message: "",
            // messages: []

        };
    }
}