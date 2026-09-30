import base64, hashlib, hmac, json

KEY = b"lesson-demo-signing-key-not-a-secret"
users = {"j.okafor": {"password": "demo-only-1", "valid_from": 0}}

def sign(body):
    return hmac.new(KEY, body, hashlib.sha256).hexdigest().encode()

def issue(user, iat):
    claims = json.dumps({"sub": user, "iat": iat}).encode()
    body = base64.urlsafe_b64encode(claims)
    return body + b"." + sign(body)

def redeem(token):
    body, sig = token.rsplit(b".", 1)
    if not hmac.compare_digest(sig, sign(body)):
        return "rejected: bad signature"
    claims = json.loads(base64.urlsafe_b64decode(body))
    if claims["iat"] < users[claims["sub"]]["valid_from"]:
        return "rejected: issued before sessions were revoked"
    return "accepted: access token for " + claims["sub"]
