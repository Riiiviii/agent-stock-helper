# Frontend

React + TypeScript + Vite application for the stock helper agent.

## Dev commands

```bash
npm install       # install dependencies
npm run dev       # start dev server with HMR
npm run build     # type-check and build for production
npm run lint      # run ESLint
npm run preview   # preview the production build locally
```

## ESLint setup

The project uses flat config (`eslint.config.js`) with:

- `@eslint/js` recommended rules
- `typescript-eslint` recommended rules
- `eslint-plugin-react-hooks` flat recommended rules
- `eslint-plugin-react-refresh` (Vite preset)

Generated files (`**/*.gen.ts`) and the `dist` folder are excluded from linting.

### Enabling type-aware lint rules

To upgrade to stricter type-checked rules, replace `tseslint.configs.recommended` in `eslint.config.js` with:

```js
tseslint.configs.recommendedTypeChecked,
// or for stricter enforcement:
tseslint.configs.strictTypeChecked,
```

and add `parserOptions` to the same config block:

```js
languageOptions: {
  globals: globals.browser,
  parserOptions: {
    project: ['./tsconfig.node.json', './tsconfig.app.json'],
    tsconfigRootDir: import.meta.dirname,
  },
},
```
