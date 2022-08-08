/**
 * Minified by jsDelivr using Terser v5.10.0.
 * Original file: /npm/promise-polyfill@8.2.3/lib/index.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
"use strict";

function finallyConstructor(e) {
    var t = this.constructor;
    return this.then((function (n) {
        return t.resolve(e()).then((function () {
            return n
        }))
    }), (function (n) {
        return t.resolve(e()).then((function () {
            return t.reject(n)
        }))
    }))
}

function allSettled(e) {
    return new this((function (t, n) {
        if (!e || void 0 === e.length) return n(new TypeError(typeof e + " " + e + " is not iterable(cannot read property Symbol(Symbol.iterator))"));
        var r = Array.prototype.slice.call(e);
        if (0 === r.length) return t([]);
        var o = r.length;

        function i(e, n) {
            if (n && ("object" == typeof n || "function" == typeof n)) {
                var s = n.then;
                if ("function" == typeof s) return void s.call(n, (function (t) {
                    i(e, t)
                }), (function (n) {
                    r[e] = {
                        status: "rejected",
                        reason: n
                    }, 0 == --o && t(r)
                }))
            }
            r[e] = {
                status: "fulfilled",
                value: n
            }, 0 == --o && t(r)
        }
        for (var s = 0; s < r.length; s++) i(s, r[s])
    }))
}
var setTimeoutFunc = setTimeout;

function isArray(e) {
    return Boolean(e && void 0 !== e.length)
}

function noop() {}

function bind(e, t) {
    return function () {
        e.apply(t, arguments)
    }
}

function Promise(e) {
    if (!(this instanceof Promise)) throw new TypeError("Promises must be constructed via new");
    if ("function" != typeof e) throw new TypeError("not a function");
    this._state = 0, this._handled = !1, this._value = void 0, this._deferreds = [], doResolve(e, this)
}

function handle(e, t) {
    for (; 3 === e._state;) e = e._value;
    0 !== e._state ? (e._handled = !0, Promise._immediateFn((function () {
        var n = 1 === e._state ? t.onFulfilled : t.onRejected;
        if (null !== n) {
            var r;
            try {
                r = n(e._value)
            } catch (e) {
                return void reject(t.promise, e)
            }
            resolve(t.promise, r)
        } else(1 === e._state ? resolve : reject)(t.promise, e._value)
    }))) : e._deferreds.push(t)
}

function resolve(e, t) {
    try {
        if (t === e) throw new TypeError("A promise cannot be resolved with itself.");
        if (t && ("object" == typeof t || "function" == typeof t)) {
            var n = t.then;
            if (t instanceof Promise) return e._state = 3, e._value = t, void finale(e);
            if ("function" == typeof n) return void doResolve(bind(n, t), e)
        }
        e._state = 1, e._value = t, finale(e)
    } catch (t) {
        reject(e, t)
    }
}

function reject(e, t) {
    e._state = 2, e._value = t, finale(e)
}

function finale(e) {
    2 === e._state && 0 === e._deferreds.length && Promise._immediateFn((function () {
        e._handled || Promise._unhandledRejectionFn(e._value)
    }));
    for (var t = 0, n = e._deferreds.length; t < n; t++) handle(e, e._deferreds[t]);
    e._deferreds = null
}

function Handler(e, t, n) {
    this.onFulfilled = "function" == typeof e ? e : null, this.onRejected = "function" == typeof t ? t : null, this.promise = n
}

function doResolve(e, t) {
    var n = !1;
    try {
        e((function (e) {
            n || (n = !0, resolve(t, e))
        }), (function (e) {
            n || (n = !0, reject(t, e))
        }))
    } catch (e) {
        if (n) return;
        n = !0, reject(t, e)
    }
}
Promise.prototype.catch = function (e) {
    return this.then(null, e)
}, Promise.prototype.then = function (e, t) {
    var n = new this.constructor(noop);
    return handle(this, new Handler(e, t, n)), n
}, Promise.prototype.finally = finallyConstructor, Promise.all = function (e) {
    return new Promise((function (t, n) {
        if (!isArray(e)) return n(new TypeError("Promise.all accepts an array"));
        var r = Array.prototype.slice.call(e);
        if (0 === r.length) return t([]);
        var o = r.length;

        function i(e, s) {
            try {
                if (s && ("object" == typeof s || "function" == typeof s)) {
                    var u = s.then;
                    if ("function" == typeof u) return void u.call(s, (function (t) {
                        i(e, t)
                    }), n)
                }
                r[e] = s, 0 == --o && t(r)
            } catch (e) {
                n(e)
            }
        }
        for (var s = 0; s < r.length; s++) i(s, r[s])
    }))
}, Promise.allSettled = allSettled, Promise.resolve = function (e) {
    return e && "object" == typeof e && e.constructor === Promise ? e : new Promise((function (t) {
        t(e)
    }))
}, Promise.reject = function (e) {
    return new Promise((function (t, n) {
        n(e)
    }))
}, Promise.race = function (e) {
    return new Promise((function (t, n) {
        if (!isArray(e)) return n(new TypeError("Promise.race accepts an array"));
        for (var r = 0, o = e.length; r < o; r++) Promise.resolve(e[r]).then(t, n)
    }))
}, Promise._immediateFn = "function" == typeof setImmediate && function (e) {
    setImmediate(e)
} || function (e) {
    setTimeoutFunc(e, 0)
}, Promise._unhandledRejectionFn = function (e) {
    "undefined" != typeof console && console && console.warn("Possible Unhandled Promise Rejection:", e)
}, module.exports = Promise;
//# sourceMappingURL=/sm/75dfb4985f308bb36f744e217bf9d0b88e5dfb87126b4f3d9a75282fbefbca88.map