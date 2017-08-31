import { SET_MESSAGES } from './mutation-types';

export default {
    [SET_MESSAGES]({ commit }, message) {
        console.log(" ::]",message);
        commit(SET_MESSAGES, message);
    }
}