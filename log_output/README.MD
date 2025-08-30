Deploy with

```
kubectl create deployment random-string-generator --image=docker.io/solitanhuttu/nhude-string-gen:latest
```

Check current pods

```
kubectl get pods
```

And tail the logs

```
kubectl logs -f random-string-generator-xxxxx-yyyyy
```
