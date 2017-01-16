import base64
import os
import sys
import yaml

SECRET_NAME = "secret-vars"
SECRET_VARS_FILE = "secret_vars.yml"
K8S_SECRETS_FILE = "secret.yml"
SECRET = ("apiVersion: v1\n"
          "kind: Secret\n"
          "metadata:\n"
          "  name: %(name)s\n"
          "type: Opaque\n"
          "data:\n"
          "%(data)s")


def main():
    if not os.path.exists(SECRET_VARS_FILE):
        sys.exit("No %s found on path, exiting" % SECRET_VARS_FILE)
    with open(SECRET_VARS_FILE, 'r') as f:
        data = yaml.load(f)
        encoded = {k: base64.b64encode(k) for k in data}
        data_str = "\n".join(["  %s: %s" % (name, value)
                              for (name, value) in encoded.iteritems()])
        with open(K8S_SECRETS_FILE, 'w') as sf:
            sf.write(SECRET % {'name': SECRET_NAME,
                               'data': data_str})


if __name__ == "__main__":
    main()
