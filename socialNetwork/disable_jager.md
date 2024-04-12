In `src/tracing.h`

```diff
diff --git a/socialNetwork/src/tracing.h b/socialNetwork/src/tracing.h
index 445d7d4..6fbf4a1 100644
--- a/socialNetwork/src/tracing.h
+++ b/socialNetwork/src/tracing.h
@@ -54,7 +54,7 @@ void SetUpTracer(
     const std::string &config_file_path,
     const std::string &service) {
   auto configYAML = YAML::LoadFile(config_file_path);
-
+  configYAML["disabled"] = true;
   // Enable local Jaeger agent, by prepending the service name to the default
   // Jaeger agent's hostname
   // configYAML["reporter"]["localAgentHostPort"] = service + "-" +
```

Reference:
- https://github.com/jaegertracing/jaeger-client-cpp/blob/e56b1bdbe89b4015d110a15115ae28775f778fca/src/jaegertracing/Config.h#L52
