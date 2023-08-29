// frontend\src\modules\authentication\authStore.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/) 
import axiosInstance from '../../plugins/connectionBuilder.js'

const authStore = {
    state: {
        isUserLoggedIn: false,
        isRegistrationProcessSucceed: false,
        registrationProcessMessage: '',
        isProcessing: false,
        loginToken: '',
        loginProcessMessage: '',
    },
    mutations: {
        setLogged(state, loginResult) {
            state.isUserLoggedIn = loginResult.success;
            state.loginToken = loginResult.token;
            state.loginProcessMessage = loginResult.message;
            if (loginResult.success) {
                // NOTE this sets the loginToken into sessionStorage
                sessionStorage.loginToken = loginResult.token;
            } else {
                sessionStorage.removeItem("loginToken");
            }
        },
        setRegistrationStatus(state, result) {
            state.isRegistrationProcessSucceed = result.success;
            sessionStorage.isRegistrationProcessSucceed = result.success;
            state.registrationProcessMessage = result.message;
        },
        setIsProcessing(state, isProcessing) {
            state.isProcessing = isProcessing
        },
        setLogout(state) {
            sessionStorage.removeItem('loginToken');
            state.isUserLoggedIn = false;
        }
    },
    actions: {
        registerNewUser({ commit, dispatch }, payload) {
            commit('setIsProcessing', true);
            axiosInstance.post('register', payload)
                .then(function (response) {
                    commit('setIsProcessing', false);
                    dispatch('toggleSnackBarvisibleAction');
                    commit('setRegistrationStatus', { success: true, message: response.data.message });

                })
                .catch(function (error) {
                    commit('setIsProcessing', false);
                    dispatch('toggleSnackBarvisibleAction');
                    if (typeof error != 'undefined' && typeof error.response != 'undefined') {
                        commit('setRegistrationStatus', { success: false, message: error.response.data.message });
                    } else {
                        commit('setRegistrationStatus', { success: false, message: error.message });
                    }
                });
        },
        authenticateUserAndSetToken({ commit, dispatch }, payload) {
            // payload is object with email and password
            console.log("authenticateUserAndSetToken function is running", payload)
            return new Promise(function (resolve, reject) {
                commit('setIsProcessing', true);
                let controllerReference = payload.controllerReference;
                delete (payload.controllerReference);
                axiosInstance.post('token', payload)
                    .then(function (response) {
                        commit('setIsProcessing', false);
                        // NOTE this code stores the login token on the front end to send back and forth in request headers 
                        // FIXME does this mean the login ends when the browser is closed?
                        commit('setLogged', { success: true, token: response.data.token, message: "Credentials accepted!" });
                        resolve(controllerReference);
                        // axiosInstance.defaults.withCredentials = true;
                        axiosInstance.defaults.headers.common['Authorization'] = response.data.token;
                    })
                    .catch(function (error) {
                        commit('setIsProcessing', false);
                        if (typeof error != 'undefined' && typeof error.response != 'undefined') {
                            commit('setLogged', { success: false, message: error.response.data.message });
                        } else {
                            commit('setLogged', { success: false, message: error.message });
                        }
                        dispatch('toggleSnackBarvisibleAction');
                        reject();
                    });
            });

        },
        setSnackbarVisibility({ commit }, isVisible) {
            commit('setIsSnackbarVisible', isVisible);
        },
        logout({ commit }, payload) {
            console.log("logout function running", payload);
            return new Promise(function (resolve, reject) {
                let controllerReference = payload.controllerReference;
                delete (payload.controllerReference);
                axiosInstance.post('logout', payload)
                    .then(function () {
                        commit('setIsProcessing', false);
                        commit('setLogout');
                        //dispatch('toggleSnackBarvisibleAction');
                        resolve(controllerReference);
                    })
                    .catch(function (error) {
                        commit('setIsProcessing', false);
                        if (typeof error != 'undefined' && typeof error.response != 'undefined') {
                            commit('setLogout');
                        } else {
                            commit('setLogout');
                        }
                        //dispatch('toggleSnackBarvisibleAction');
                        reject();
                    });
            });
        }
    },
    getters: {
        getIsRegistrationProcessSucceed(state) {
            if (state.registrationProcessMessage === '') {
                return undefined;
            } else {
                return state.isRegistrationProcessSucceed;
            }

        },
        getRegistrationProcessMessage(state) {
            return state.registrationProcessMessage;
        },
        getLoginProcessMessage(state) {
            return state.loginProcessMessage;
        },
        isProcessing(state) {
            return state.isProcessing;
        },
        getIsUserLoggedIn(state) {
            // console.log(state.isUserLoggedIn)
            if (state.isUserLoggedIn === false) {
                if (sessionStorage.loginToken) {
                    return true;
                }
                return false;
            }
            return true;
        }
    }
}

export default authStore;